from django.test import TestCase
from applications.account.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


class ProductTest(TestCase):
    @property
    def bearer_token(self):
        user, created = CustomUser.objects.get_or_create(email="feelingjeez@gmail.com", password="red124566", is_active=True)
        refresh = RefreshToken.for_user(user)
        return {"HTTP_AUTHORIZATION":f"Bearer {refresh.access_token}"}
    
    # def test_product_post(self):
    #     url = "http://127.0.0.1:8000/api/v1/product/"
    #     response = self.client.post(url, data={"name": "test", "category": "Education", "price": "1200", "amount": "2"}, **self.bearer_token)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED, "Wrong data, please enter data correctly")
        
    def test_product_patch(self):
        url = "http://127.0.0.1:8000/api/v1/product/"
        response = self.client.post(url, data={"name": "test", 
                                               "category": "Education", 
                                               "price": "1200", 
                                               "amount": "2"}, 
                                            **self.bearer_token)
        
        retrieve_url = "http://127.0.0.1:8000/api/v1/product/1/"
        response = self.client.patch(retrieve_url, data={
                "name": "cars", 
                "category": "Sports", 
            }, 
            content_type='application/json',
            **self.bearer_token
        )
        # self.assertEqual(response.status_code, status.HTTP_200_OK, "Wrong data, please enter data correctly")
        print(response.data)
        
    # def test_product_get(self):
    #     url = "http://127.0.0.1:8000/api/v1/product/"
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)