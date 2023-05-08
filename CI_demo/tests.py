from django.test import TestCase

# Create your tests here.
class TestHomePageView(TestCase):
    def test_reachable_home(self):
        response = self.client.get('/CI_demo/home')
        self.assertEqual(response.status_code,200)