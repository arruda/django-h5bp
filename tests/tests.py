from django.test import TestCase

from django.template.loader import Template, Context


class TemplateTestCase(TestCase):
    BASE_TEMPLATE = """ """

    def setUp(self):
        self.template_txt = self.BASE_TEMPLATE

    def test_can_override_django_h5bp_css_block(self):
        context = Context({})
        self.template_txt += """

        {% block django-h5bp-css %}<div>NO-BOCK</div>{% endblock %}
        """
        template = Template(self.template_txt)
        rendered = template.render(context)
        self.assertInHTML(
            """<div>NO-BOCK</div>""",
            rendered,
            msg_prefix="Could not override django-h5bp-css block. "
        )

    def test_can_override_django_h5bp_js_block(self):
        context = Context({})
        self.template_txt += """

        {% block django-h5bp-js %}<div>NO-BOCK</div>{% endblock %}
        """
        template = Template(self.template_txt)
        rendered = template.render(context)
        self.assertInHTML(
            """<div>NO-BOCK</div>""",
            rendered,
            msg_prefix="Could not override django-h5bp-js block. "
        )


class BootstrapTeamplateTest(TemplateTestCase):
    BASE_TEMPLATE = """
        {% extends "bootstrap/bootstrap_h5bp.html" %}
        """


class ClassicTeamplateTest(TemplateTestCase):
    BASE_TEMPLATE = """
        {% extends "classic/classic_h5bp.html" %}
        """


class ResponsiveTeamplateTest(TemplateTestCase):
    BASE_TEMPLATE = """
        {% extends "responsive/responsive_h5bp.html" %}
        """
