from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

from applications.product.models import Product

User = get_user_model()

# class CommentTest(TestCase):
#     def setUp(self) -> None:
#         User.objects.create(email='dcabatar@gmail.com', password='123456', is_active = True)
#         Product.objects.create(name='test_product', price=100, category='Education', amount=100, owner=User.objects.get(email='dcabatar@gmail.com'))
#         self.data = dict(product=Product.objects.get(name='test_product').id, comment ='hello')
        
#     @property
#     def jwt_token(self):
#         user1 = User.objects.get(email='dcabatar@gmail.com')
#         refresh = RefreshToken.for_user(user1)
#         return {'HTTP_AUTHORIZATION':f'Bearer {refresh.access_token}'}
    
    
#     def test_get_comment(self):
#         url = 'http://127.0.0.1:8000/api/v1/feedback/comment/'
#         response = self.client.get(url, **self.jwt_token)
        
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
        
        
#     def test_post_comment(self):
#         url = 'http://127.0.0.1:8000/api/v1/feedback/comment/'
#         response = self.client.post(url, data=self.data, **self.jwt_token)
        
#         self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        
        
#     def test_put_comment(self):
#         url = 'http://127.0.0.1:8000/api/v1/feedback/comment/'
#         response = self.client.post(url, data=self.data, **self.jwt_token)
        
#         url = f'http://127.0.0.1:8000/api/v1/feedback/comment/{response.data["id"]}/'
#         data1 = dict(product=Product.objects.get(name='test_product').id, comment ='hi')
#         response = self.client.put(url, data=data1, **self.jwt_token, content_type='application/json')
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
        
        
#     def test_delete_comment(self):
#         url = 'http://127.0.0.1:8000/api/v1/feedback/comment/'
#         response = self.client.post(url, data=self.data, **self.jwt_token)
        
#         url = f'http://127.0.0.1:8000/api/v1/feedback/comment/{response.data["id"]}/'
#         response = self.client.delete(url, **self.jwt_token, content_type='application/json')
#         self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        
        
    
class RatingTest(TestCase):
    def setUp(self) -> None:
        User.objects.create(email='dcabatar@gmail.com', password='123456', is_active = True)
        Product.objects.create(name='test_product', price=100, category='Education', amount=100, owner=User.objects.get(email='dcabatar@gmail.com'))
        self.data = dict(product=Product.objects.get(name='test_product').id, rating = 4)
        
    @property
    def jwt_token(self):
        user1 = User.objects.get(email='dcabatar@gmail.com')
        refresh = RefreshToken.for_user(user1)
        return {'HTTP_AUTHORIZATION':f'Bearer {refresh.access_token}'}
    
    
    def test_post_rating(self):
        url = f'http://127.0.0.1:8000/api/v1/product/{Product.objects.get(name="test_product").id}/rating/'
        response = self.client.post(url, data=self.data, **self.jwt_token)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        
        
    def test_delete_rating(self):
        url = f'http://127.0.0.1:8000/api/v1/product/{Product.objects.get(name="test_product").id}/rating/'
        response = self.client.post(url, data=self.data, **self.jwt_token)
        
        url = f'http://127.0.0.1:8000/api/v1/product/{Product.objects.get(name="test_product").id}/rating_delete/'
        response = self.client.delete(url, **self.jwt_token)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        
    
    def test_put_rating(self):
        url = url = f'http://127.0.0.1:8000/api/v1/product/{Product.objects.get(name="test_product").id}/rating/'
        response = self.client.post(url, data=self.data, **self.jwt_token)
        
        new_rating = dict(product=Product.objects.get(name='test_product').id, rating = 5)
        url = f'http://127.0.0.1:8000/api/v1/product/{Product.objects.get(name="test_product").id}/rating_update/'
        response = self.client.put(url, data=new_rating, **self.jwt_token, content_type='application/json')
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        
        
    
# class LikeUnlikeTest(TestCase):
#     def setUp(self) -> None:
#         User.objects.create(email='dcabatar@gmail.com', password='123456', is_active = True)
#         Product.objects.create(name='test_product', price=100, category='Education', amount=100, owner=User.objects.get(email='dcabatar@gmail.com'))
#         self.data = dict(product=Product.objects.get(name='test_product').id)
        
#     @property
#     def jwt_token(self):
#         user1 = User.objects.get(email='dcabatar@gmail.com')
#         refresh = RefreshToken.for_user(user1)
#         return {'HTTP_AUTHORIZATION':f'Bearer {refresh.access_token}'}
    
    
#     def test_post_like(self):
#         url = f'http://127.0.0.1:8000/api/v1/product/{Product.objects.get(name="test_product").id}/like/'
#         response = self.client.post(url, data=self.data, **self.jwt_token)
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
        
    
#     def test_post_unlike(self):
#         url = f'http://127.0.0.1:8000/api/v1/product/{Product.objects.get(name="test_product").id}/unlike/'
#         response = self.client.post(url, data=self.data, **self.jwt_token)
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
        
        
    
    
# class RecommendTest(TestCase):
#     def setUp(self) -> None:
#         User.objects.create(email='dcabatar@gmail.com', password='123456', is_active = True)
#         Product.objects.create(name='test_product', price=100, category='Education', amount=100, owner=User.objects.get(email='dcabatar@gmail.com'))
#         self.data = dict(product=Product.objects.get(name='test_product').id)
        
#     @property
#     def jwt_token(self):
#         user1 = User.objects.get(email='dcabatar@gmail.com')
#         refresh = RefreshToken.for_user(user1)
#         return {'HTTP_AUTHORIZATION':f'Bearer {refresh.access_token}'}
    
    
#     def test_get_recommend(self):
#         url = f'http://127.0.0.1:8000/api/v1/product/{Product.objects.get(name="test_product").id}/recommend/'
#         response = self.client.get(url)
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
        
        
    
# class FansTest(TestCase):
#     def setUp(self) -> None:
#         User.objects.create(email='dcabatar@gmail.com', password='123456', is_active = True)
#         Product.objects.create(name='test_product', price=100, category='Education', amount=100, owner=User.objects.get(email='dcabatar@gmail.com'))
#         self.data = dict(product=Product.objects.get(name='test_product').id)
        
#     @property
#     def jwt_token(self):
#         user1 = User.objects.get(email='dcabatar@gmail.com')
#         refresh = RefreshToken.for_user(user1)
#         return {'HTTP_AUTHORIZATION':f'Bearer {refresh.access_token}'}
    
    
#     def test_get_fans(self):
#         url = f'http://127.0.0.1:8000/api/v1/product/{Product.objects.get(name="test_product").id}/get_fans/'
#         response = self.client.get(url)
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
    
        
        
        
        
        
    
        
        
        
        
        
    