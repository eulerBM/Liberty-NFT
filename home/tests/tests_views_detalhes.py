from django.test import Client, TestCase
from django.urls import reverse
from autor.models import items, Saldo
from django.contrib.auth.models import User
from datetime import datetime
from unittest.mock import patch, Mock

class DetailsViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.item = items.objects.create(
            user=self.user,
            Nome='test item',
            Preco=1,
            data_atual=datetime.now()
        )
        self.url = reverse('details', args=[self.item.id])
        self.eth_price = 1000
        self.response_mock = Mock()
        self.response_mock.json.return_value = {"BRL": self.eth_price}

    def test_details_view(self):
        with patch('requests.get', return_value=self.response_mock) as mocked_get:
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'details.html')
            item = response.context['item']
            self.assertEqual(item, self.item)
            eth_price = response.context['eth']
            expected_eth_price = '{:,.2f}'.format(int(self.item.Preco * self.eth_price))
            self.assertEqual(eth_price, expected_eth_price)
            saldo = response.context['saldo']
            self.assertEqual(saldo, '0')
            item_2 = response.context['item_2']
            self.assertQuerysetEqual(item_2, items.objects.all()[:6], transform=lambda x: x)

