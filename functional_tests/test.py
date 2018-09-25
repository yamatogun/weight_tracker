from selenium import webdriver
from django.test import TestCase
from selenium.webdriver.common.keys import Keys


class WeightTrackerTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Weight Tracker', self.browser.title)

        input = self.browser.find_element_by_id('weight_entry')
        input.send_keys('60')
        input.send_keys(Keys.Keys.ENTER)

        time.sleep(1)

        ul = self.browser.find_element_by_id('ul')
        weight_entries = table.find_element_by_class_name('li')
        self.assertIn('60', weight_entries)

        self.fail('--- end of tests ---')
