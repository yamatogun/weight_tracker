from django.test import TestCase
from weight_tracker.views import home_page

from django.urls import resolve

class TestHomePage(TestCase):
    def test_home_page_displays_properly(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

        html = response.content.decode('utf8')
        self.assertIn('Weight Tracker', html)
