from app.plugins import TestSuiteAnalyser, SpecificationAnalyser, ReportsAnalyser, JinjaReporter
from config import settings
import json


def run():
        
    for suite in settings.SUITE_TO_SPEC_MAPPINGS:
        report_url = settings.TEST_SUITES[suite]
        specification_urls = [
            settings.SPECIFICATIONS[spec]
            for spec in settings.SUITE_TO_SPEC_MAPPINGS[suite]
        ]
        suite_statements = TestSuiteAnalyser().fetch_statements(report_url)
        suite_statements_copy = suite_statements.copy()
        spec_statements = []
        for spec_url in specification_urls:
            # grouped, listed = SpecificationAnalyser().fetch_normative_statements(spec_url)
            # spec_statements += listed
            spec_statements += SpecificationAnalyser().fetch_statements(
                spec_url
            )
        spec_statements = list(dict.fromkeys(spec_statements))
        spec_statements_copy = spec_statements.copy()
        matched_statements = TestSuiteAnalyser().match_statements(
            suite_statements_copy, spec_statements_copy
        )
        coverage_metrics = TestSuiteAnalyser().derive_metrics(matched_statements, suite_statements, spec_statements)
        coverage_metrics['suite'] = suite
        coverage_metrics['unmatched_suite_statements'] = {
            'count': len(suite_statements_copy),
            'list': json.dumps(suite_statements_copy, indent=2)
        }
        coverage_metrics['unmatched_spec_statements'] = {
            'count': len(spec_statements_copy),
            'list': json.dumps(spec_statements_copy, indent=2)
        }
        risk_metrics = ReportsAnalyser().get_rows(report_url)
        coverage_metrics['risk'] = risk_metrics
        template = JinjaReporter().render_template('coverage_metrics', coverage_metrics)
        with open(f"outputs/{suite}.md", "w+") as f:
            f.write(template)

