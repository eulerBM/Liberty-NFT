from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from criar.models import *
from autor.models import *
from datetime import date
import requests

class CriarViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Cria um usuário de teste para autenticar nos testes
        User.objects.create_user(username='testuser', password='12345')

    def setUp(self):
        self.client = Client()
        self.client.login(username='testuser', password='12345')

    def test_criar_view_with_valid_form_data(self):
        # Cria um objeto Saldo para o usuário de teste
        saldo = Saldo.objects.create(user=User.objects.get(username='testuser'), saldo=1000)
        url = reverse('criar')
        eth_price = requests.get("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BRL").json()["BRL"]
        data = {
            'name': 'Item de Teste',
            'Preco': 0.1,
            'descricao': 'Descrição do item de teste',
            'data_atual': date.today(),
        }
        response = self.client.post(url, data, follow=True)
        # Verifica que a view redirecionou para a página 'criar'
        self.assertRedirects(response, reverse('criar'))
        # Verifica que a mensagem de sucesso foi exibida na página
        self.assertContains(response, 'Item cadastrado com sucesso.')
        # Verifica que o objeto foi salvo no banco de dados
        self.assertTrue(items.objects.filter(user=User.objects.get(username='testuser')).exists())
        # Verifica que o saldo do usuário foi atualizado
        self.assertEqual(Saldo.objects.get(user=User.objects.get(username='testuser')).saldo, 1000 - (0.1 * eth_price))

    def test_criar_view_with_invalid_form_data(self):
        # Cria um objeto Saldo para o usuário de teste
        saldo = Saldo.objects.create(user=User.objects.get(username='testuser'), saldo=1000)
        url = reverse('criar')
        data = {
            'name': '',
            'Preco': -1,
            'descricao': '',
            'data_atual': date.today(),
        }
        response = self.client.post(url, data, follow=True)
        # Verifica que a view exibiu a página 'criar'
        self.assertTemplateUsed(response, 'create.html')
        # Verifica que a mensagem de erro foi exibida na página
        self.assertContains(response, 'Nome é um campo obrigatório.')
        # Verifica que o objeto não foi salvo no banco de dados
        self.assertFalse(items.objects.filter(user=User.objects.get(username='testuser')).exists())
        # Verifica que o saldo do usuário não foi atualizado
        self.assertEqual(Saldo.objects.get(user=User.objects.get(username='testuser')).saldo, 1000)
