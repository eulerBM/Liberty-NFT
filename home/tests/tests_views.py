from django.test import TestCase
from django.urls import reverse

class url_TestCase(TestCase):

    # Testa as as URLS

    def test_url_home_retorna_200(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
    
    def test_url_explore_retorna_200(self):
        response = self.client.get(reverse('explore'))
        self.assertEquals(response.status_code, 200)

    def test_url_details_retorna_200(self):
        response = self.client.get(reverse('details'))
        self.assertEquals(response.status_code, 200)

    def test_url_create_retorna_200(self):
        response = self.client.get(reverse('create'))
        self.assertEquals(response.status_code, 200)

    def test_url_author_retorna_200(self):
        response = self.client.get(reverse('author'))
        self.assertEquals(response.status_code, 200)

    
        

# Create your tests here.
