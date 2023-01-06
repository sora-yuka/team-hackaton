from django.test import TestCase
from rest_framework import status
from applications.product.models import Product
from applications.account.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse


class FavoriteTest(TestCase):
    def setUp(self):
        CustomUser.objects.create(email="example@mail.com", password="qwerty", is_active=True)
        self.product = Product.objects.create(name="Test", price=1000, category="Education", amount=2, owner=CustomUser.objects.get(email="example@mail.com"))
        
    @property
    def bearer_token(self):
        user = CustomUser.objects.get(email="example@mail.com")
        refresh = RefreshToken.for_user(user)
        return {"HTTP_AUTHORIZATION": f"Bearer {refresh.access_token}"}
    
    
    def test_favorite_get(self):
        response = self.client.get(self.url, **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_favorite_post(self):
        response = self.client.post(self.url, data={"product": "1"}, **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_favorite_retrieve(self):
        url = "http://127.0.0.1:8000/api/v1/favorites/"
        response = self.client.post(url, data={"product": "1"}, **self.bearer_token)
        
        url = f"http://127.0.0.1:8000/api/v1/favorites/{response.data['id']}/"
        response = self.client.get(url, **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_favorite_destroy(self):
        url = "http://127.0.0.1:8000/api/v1/favorites/"
        response = self.client.post(url, data={"product": 1}, **self.bearer_token)
        
        url = f"http://127.0.0.1:8000/api/v1/favorites/{response.data['id']}/"
        response = self.client.delete(url, **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)