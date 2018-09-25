from django.test import TestCase
from django.urls import resolve, reverse

from weight_tracker.models import Weight
from weight_tracker.views import home_page


class TestHomePage(TestCase):
    def test_home_page_displays_properly(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

        html = response.content.decode('utf8')
        self.assertIn('Weight Tracker', html)

    def test_post_create_weight_and_redirect(self):
        # TODO: change test name
        response = self.client.post('/', data={'new_weight': 50})

        self.assertEqual(Weight.objects.count(), 1)
        weight = Weight.objects.first()
        self.assertEqual(weight.value, 50)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_multiple_weight_can_be_saved(self):
        Weight.objects.create(value=60)
        Weight.objects.create(value=70)

        self.assertEqual(Weight.objects.count(), 2)

        home_url = reverse('Home')
        response = self.client.get(home_url)
        self.assertContains(response, '60')
        self.assertContains(response, '70')


class TestWeightModel(TestCase):
    pass
