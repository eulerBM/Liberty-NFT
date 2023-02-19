from django.test import TestCase
from django.urls import reverse
from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from autor.models import Seguir
from autor.views import author, conta_de_outro_user, seguir, deixar_de_seguir


class AuthorViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.url = reverse('author')

    def test_author_view_with_get_request(self):
        request = self.factory.get(self.url)
        request.user = self.user

        response = author(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author.html')
        self.assertContains(response, 'My items')

    def test_conta_de_outro_user_view_with_get_request(self):
        another_user = User.objects.create_user(username='anotheruser', email='another@example.com', password='testpass')
        request = self.factory.get(reverse('outro_user', args=[another_user.pk]))
        request.user = self.user

        response = conta_de_outro_user(request, another_user.pk)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author_user.html')
        self.assertContains(response, 'Another User Items')

    def test_seguir_view_with_valid_id(self):
        another_user = User.objects.create_user(username='anotheruser', email='another@example.com', password='testpass')
        request = self.factory.get(reverse('seguir', args=[another_user.pk]))
        request.user = self.user

        response = seguir(request, another_user.pk)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Seguir.objects.filter(seguidor=self.user, seguido=another_user).count(), 1)

    def test_seguir_view_with_same_id(self):
        request = self.factory.get(reverse('seguir', args=[self.user.pk]))
        request.user = self.user

        response = seguir(request, self.user.pk)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Seguir.objects.filter(seguidor=self.user, seguido=self.user).count(), 0)

    def test_deixar_de_seguir_view_with_valid_id(self):
        another_user = User.objects.create_user(username='anotheruser', email='another@example.com', password='testpass')
        Seguir.objects.create(seguidor=self.user, seguido=another_user)
        request = self.factory.get(reverse('deixar_de_seguir', args=[another_user.pk]))
        request.user = self.user

        response = deixar_de_seguir(request, another_user.pk)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Seguir.objects.filter(seguidor=self.user, seguido=another_user).count(), 0)
        







    

    
        


