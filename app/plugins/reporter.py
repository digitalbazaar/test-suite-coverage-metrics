from jinja2 import Environment, PackageLoader, select_autoescape


class JinjaReporter:
    def __init__(self):
        self.env = Environment(loader=PackageLoader("app"), autoescape=select_autoescape())
        
    def render_template(self, template_name, data):
        template = self.env.get_template(f'{template_name}.jinja')
        return template.render(data=data)
        
    def render_charts(self, data):
        total_spec_statements = []
        total_suite_statements = []
        total_skip_statements = []
        suite_minus_skip_statements = []
        suite_to_spec_statements = []
        unmatched_spec_statements = []
        unmatched_suite_statements = []
        charts = {
            'spec_to_suite': {
                'spec': len(total_spec_statements),
                'suite': len(total_suite_statements),
            },
            'match': {
                'spec': len(total_spec_statements),
                'match': len(suite_to_spec_statements)
            },
            'unmatched': {
                'spec': len(unmatched_spec_statements),
                'suite': len(unmatched_suite_statements),
            },
            'skipped': {
                'skip': len(total_skip_statements),
                'spec': len(suite_minus_skip_statements),
            },
        }
        template = self.env.get_template('components/charts.jinja')
        return template.render(charts=charts)