from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.mixins import CreateModelMixin
from applications.order.models import Order

from applications.product.models import Product

User = get_user_model()

class OrderTest(TestCase):
    def setUp(self) -> None:
        User.objects.create(email='dcabatar@gmail.com', password='123456', is_active = True)
        Product.objects.create(name='test_product', price=100, category='Education', amount=100, owner=User.objects.get(email='dcabatar@gmail.com'))
        self.data = dict(product=Product.objects.get(name='test_product').id, amount=10, number=996701750707, address='Bishkek', is_confirm=True)
        
    @property
    def jwt_token(self):
        user1 = User.objects.get(email='dcabatar@gmail.com')
        refresh = RefreshToken.for_user(user1)
        return {'HTTP_AUTHORIZATION':f'Bearer {refresh.access_token}'}
        
    def test_get_order(self):
        url = 'http://127.0.0.1:8000/api/v1/order/'
        response = self.client.get(url)
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        
    
    def test_post_order(self):
        
        url = 'http://127.0.0.1:8000/api/v1/order/'
        response = self.client.post(url, data=self.data, **self.jwt_token)
        
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        
    
    
    def test_get_detail_order(self):
        url = 'http://127.0.0.1:8000/api/v1/order/'  
        response = self.client.post(url, data=self.data, **self.jwt_token)
        print(response.data)

        url = f'http://127.0.0.1:8000/api/v1/order/{response.data["id"]}/'
        response = self.client.get(url, **self.jwt_token)
        print(response.data)
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        
        
        