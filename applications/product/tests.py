from django.test import TestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()

class ProductTestCase(TestCase):
    def setUp(self) -> None:
        User.objects.create(email='dcabatar@gmail.com', password='123456', is_active = True)
        self.data = dict(name='post', price=100, category='Education', amount=100, owner=User.objects.get(email='dcabatar@gmail.com'))
        
    @property
    def jwt_token(self):
        user1 = User.objects.get(email='dcabatar@gmail.com')
        refresh = RefreshToken.for_user(user1)
        return {'HTTP_AUTHORIZATION':f'Bearer {refresh.access_token}'}
    
    
    def test_product_post(self):  
        url = 'http://127.0.0.1:8000/api/v1/product/'
        response = self.client.post(url, data=self.data, **self.jwt_token)
        
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        
        
    def test_product_get(self):
        url = 'http://127.0.0.1:8000/api/v1/product/'
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        
    
    def test_product_get_detail(self):
        url = 'http://127.0.0.1:8000/api/v1/product/'
        response = self.client.post(url, data=self.data, **self.jwt_token)
        
        url = f'http://127.0.0.1:8000/api/v1/product/{response.data["id"]}/'
        response = self.client.get(url)
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        
     
    def test_product_put(self):    
        url = 'http://127.0.0.1:8000/api/v1/product/'
        response = self.client.post(url, data=self.data, **self.jwt_token)
        
        data1 = {'name':'put', 'price':1500, 'category':'Education', 'amount': 50}
        url = f'http://127.0.0.1:8000/api/v1/product/{response.data["id"]}/'
        response = self.client.put(url, data=data1, **self.jwt_token, content_type='application/json')
    
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        
        
    def test_product_patch(self):      
        url = 'http://127.0.0.1:8000/api/v1/product/'
        response = self.client.post(url, data=self.data, **self.jwt_token)
        
        data1 = {'name':'patch', 'category':'Education', 'amount': 50}
        url = f'http://127.0.0.1:8000/api/v1/product/{response.data["id"]}/'
        response = self.client.patch(url, data=data1, **self.jwt_token, content_type='application/json')
    
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        
        
    def test_product_delete(self):
        url = 'http://127.0.0.1:8000/api/v1/product/'
        response = self.client.post(url, data=self.data, **self.jwt_token)
        
        url = f'http://127.0.0.1:8000/api/v1/product/{response.data["id"]}/'
        response = self.client.delete(url, **self.jwt_token, content_type='application/json')
        
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)