from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(title="Pizza", price=20, inventory=50)
        Menu.objects.create(title="Burger", price=15, inventory=30)

    def test_getall(self):
        client = APIClient()

        response = client.get('/api/menu-items/')

        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)