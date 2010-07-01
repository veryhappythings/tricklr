from django.test import TestCase
from django.test.client import Client

class TestTrickleList(TestCase):
    def setup(self):
        self.client = Client()

    def test_404(self):
        response = self.client.get('/this_does_not_exist!/')
        self.assertEqual(response.status_code, 404)

    def test_that_index_page_exists(self):
        response = self.client.get('/trickle/')
        self.assertEqual(response.status_code, 200)

