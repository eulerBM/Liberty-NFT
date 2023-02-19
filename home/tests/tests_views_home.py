from django.test import TestCase, Client
from django.urls import reverse
from criar.models import *
from autor.models import *

class HomeViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'bd_all')
        self.assertContains(response, 'bd_item')
        self.assertContains(response, 'saldo')
