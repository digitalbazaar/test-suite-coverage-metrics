from typing import List
from urllib.request import urlopen
from bs4 import BeautifulSoup, SoupStrainer
from difflib import SequenceMatcher, get_close_matches
import json
import copy

class BaseAnalyser:
    def _soup(self, url):
        return BeautifulSoup(urlopen(url).read().decode("utf-8"), "html.parser")


class SpecificationAnalyser(BaseAnalyser):
    def __init__(self):
        self.section_classes = ['introductory', 'informative', 'appendix', 'normative']
    
    def _parse_statement(self, statement):
        statement = " ".join(statement.get_text().split())
        statement = statement.replace('"', "'")
        statement = statement.split(". ")
        statement = statement if isinstance(statement, list) else []
        for item in statement.copy():
            # keywords = ['MAY', 'MUST', 'REQUIRED', 'OPTIONAL', 'SHOULD']
            keywords = ["MUST"]
            if all(word not in item for word in keywords):
                statement.remove(item)
        return statement
    
    def _find_rfc2119(self, section):
        statements = []
        for tag in section.find_all("em", {"class": "rfc2119"}):
            if tag.find_parent():
                statements += self._parse_statement(tag.find_parent())
        statements = list(dict.fromkeys(statements))
        return statements
    
    def _add_if_new(self, statements, processed_statements):
        return [statement for statement in statements if statement not in processed_statements]
    
    # def _parse_sections(self, section):

    def fetch_normative_statements(self, spec_url):
        soup = self._soup(spec_url)
        output = {}
        normative_sections = soup.find_all(attrs={"class": "normative"})
        processed_statements = []
        # Go through every normative flagged section
        for section in normative_sections:
            section_id = section.get('id')
            child_sections = section.findChildren("section")
            parent_section = section.find_parent("section")
                
            # If section is not embedded, look for child sections
            if not parent_section:
                output[section_id] = {}
                child_sections = section.findChildren("section")
                # If present, embed child under section
                for child_section in child_sections:
                    child_id = child_section.get('id')
                    if child_id:
                        output[section_id][child_id] = {
                            '_statements': self._add_if_new(self._find_rfc2119(child_section), processed_statements)
                        }
                        processed_statements += output[section_id][child_id]['_statements']
                output[section_id]['_statements'] = self._add_if_new(self._find_rfc2119(section), processed_statements)
                processed_statements += output[section_id]['_statements']
            
            # If section is embedded, nest it under parent section
            if parent_section:
                parent_id = parent_section.get('id')
                if parent_id not in output:
                    output[parent_id] = {}
                output[parent_id][section_id] = {
                    '_statements': self._add_if_new(self._find_rfc2119(section), processed_statements)
                }
                processed_statements += output[parent_id][section_id]['_statements']
                output[parent_id]['_statements'] = self._add_if_new(self._find_rfc2119(parent_section), processed_statements)
                processed_statements += output[parent_id]['_statements']
        return output, processed_statements
            

    def fetch_statements(self, spec_url):
        soup = self._soup(spec_url)
        statements = []
        # statements = SoupStrainer('em',{'class': 'rfc2119'})
        parent_tags = list(
            dict.fromkeys(
                [tag.find_parent() for tag in soup.find_all("em", {"class": "rfc2119"})]
            )
        )

        for tag in parent_tags:
            tag_statements = " ".join(tag.get_text().split())
            tag_statements = tag_statements.replace('"', "'")
            tag_statements = tag_statements.split(". ")
            for item in tag_statements.copy():
                # keywords = ["MAY", "MUST", "REQUIRED", "OPTIONAL", "SHOULD"]
                keywords = ["MUST", "REQUIRED"]
                if all(word not in item for word in keywords):
                    tag_statements.remove(item)
            statements += tag_statements
        return list(dict.fromkeys(statements))[1:]


class TestSuiteAnalyser(BaseAnalyser):

    def fetch_statements(self, report_url):
        soup = self._soup(report_url)
        test_suite_statements = [
            tag.text for tag in soup.find(id="conformance").find_all("a")
        ]
        return test_suite_statements

    def match_statements(self, suite_statements, combined_spec_statements):
        matches = []
        for x in range(5):
            for spec_statement in combined_spec_statements:
                for test_statement in suite_statements:
                    if SequenceMatcher(None, spec_statement, test_statement).ratio() >= 0.75:
                        matches.append((spec_statement,test_statement))
                        suite_statements.remove(test_statement)
                        combined_spec_statements.remove(spec_statement)
                        break
        return matches
    
    def derive_metrics(self, matches, suite_statements, spec_statements):
        return {
            'spec_statements': {
                'count': len(spec_statements),
                'list': json.dumps(spec_statements, indent=2),
            },
            'suite_statements': {
                'count': len(suite_statements),
                'list': json.dumps(suite_statements, indent=2),
            },
            'matches': {
                'count': len(matches),
                'list': json.dumps(matches, indent=2)
            },
            'coverage': str(
                int(
                    100
                    * (len(spec_statements) - (len(spec_statements)-len(matches)))
                    / len(spec_statements)
                )
            ) + ' %',
        }

class ReportsAnalyser(BaseAnalyser):
    # def __init__(self):
    #     self.section_classes = ['introductory', 'informative', 'appendix', 'normative']
    def get_rows(self, report_url):
        soup = self._soup(report_url)
        tables = soup.findChildren('table')
        sections = {}
        pending_features = []
        at_risk_features = []
        at_risk_count = 0
        total_count = 0
        
        # Skip the Key table
        for table in tables[1:]:
            section = table.findParent('section').get('id')
            if 'interop' in section:
                pass
            else:
                sections[section] = {}
                table_body = table.findChildren('tbody')[0]
                table_rows = table_body.findChildren('tr')
                for row in table_rows:
                    try:
                        statement = row.findChildren('td')[0].findChildren('a')[0].string
                    except:
                        statement = row.findChildren('td')[0].string
                    passed = row.findChildren('td', attrs={"class": "passed"})
                    failed = row.findChildren('td', attrs={"class": "failed"})
                    pending = row.findChildren('td', attrs={"class": "pending"})
                    if len(pending) == len(row.findChildren('td')[1:]):
                        pending_features.append(statement.strip())
                        sections[section][statement] = {
                            'atRisk': False,
                            'passed': len(passed),
                            'failed': len(failed),
                            'pending': len(pending),
                        }
                    else:
                        sections[section][statement] = {
                            'atRisk': True if len(passed) < 2 else False,
                            'passed': len(passed),
                            'failed': len(failed),
                            'pending': len(pending),
                        }
                        if sections[section][statement]['atRisk']:
                            at_risk_features.append(statement.strip())
                    at_risk_count += 1 if sections[section][statement]['atRisk'] else 0
                    total_count += 1
        percentage = int(100 * float(at_risk_count)/float(total_count))
        if percentage == 0:
            risk = 'No Risk'
        elif percentage < 5:
            risk = 'Low'
        elif percentage < 10:
            risk = 'Medium'
        elif percentage < 20:
            risk = 'High'
        elif percentage < 40:
            risk = 'Severe'
        elif percentage > 50:
            risk = 'Critical'
        return {
            'atRiskFeatures': at_risk_features,
            'pendingFeatures': pending_features,
            'atRiskCount': at_risk_count,
            'totalCount': total_count,
            'atRiskPercentage': percentage,
            'atRiskScore': risk,
            'results': sections
        }