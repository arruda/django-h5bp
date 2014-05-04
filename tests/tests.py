from django.test import TestCase

from django.template.loader import Template, Context


class BootstrapTeamplteTest(TestCase):
    BASE_TEMPLATE = """
        {% extends "bootstrap/bootstrap_h5bp.html" %}
        """

    def setUp(self):
        self.template_txt = self.BASE_TEMPLATE

    def test_bla(self):
        context = Context({"my_name": "Adrian"})
        template = Template(self.template_txt)
        rendered = template.render(context)
        self.assertInHTML("""<script src="/static/js/main.js">""", rendered)
