from selenium import webdriver
from django.test import TestCase


class WeightTrackerTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        self.fail('--- end of tests ---')
