from jinja2 import Environment, PackageLoader, select_autoescape


class JinjaReporter:
    def __init__(self):
        self.env = Environment(loader=PackageLoader("app"), autoescape=select_autoescape())
        
    def render_template(self, template_name, data):
        template = self.env.get_template(f'{template_name}.jinja')
        return template.render(data=data)