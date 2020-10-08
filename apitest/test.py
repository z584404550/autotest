from .views import home, login
from django.urls import reverse
from django.http import HttpRequest
from django.test import TestCase


class TitlePageTest(TestCase):
    def test_loginpage_return_title_html(self):
        request = HttpRequest()
        response = login(request)
        self.assertIn(b'<title>AutotestPlat</title>', response.content)
