from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from autor.models import items

class ExploreViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.item = items.objects.create(titulo='test item', preco=10)
        
    def test_explore_with_keyword(self):
        request = self.factory.get(reverse('explore'))
        request.user = self.user
        request.GET['keyword'] = 'test item'
        
        response = (request)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'explore.html')
        self.assertIn('items_filter', response.context)
        self.assertNotIn('items', response.context)
        self.assertEqual(response.context['items_filter'].count(), 1)
        self.assertEqual(response.context['items_filter'][0], self.item)
        
    def test_explore_without_keyword(self):
        request = self.factory.get(reverse('explore'))
        request.user = self.user
        
        response = (request)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'explore.html')
        self.assertIn('items', response.context)
        self.assertNotIn('items_filter', response.context)
        self.assertEqual(response.context['items'].count(), 5)
