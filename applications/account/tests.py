import uuid
from django.urls import reverse
from rest_framework.test import APITestCase
from applications.account.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


class AccountTests(APITestCase):
    @property
    def example_bearer_token(self):
        user = CustomUser.objects.create_user(email="example@mail.com",
                                              password="qwerty", 
                                              is_active=True)
        refresh = RefreshToken.for_user(user)
        return {"HTTP_AUTHORIZATION": f"Bearer {refresh.access_token}"}
    
    @property
    def trial_bearer_token(self):
        user = CustomUser.objects.create_user(email="feelingjeez@gmail.com",
                                              password="qwerty",
                                              is_active=True)
        refresh = RefreshToken.for_user(user)
        return {"HTTP_AUTHORIZATION": f"Bearer {refresh.access_token}"}
    
    @property
    def bearer_token(self):
        print("\nPlease enter working email address again")
        user = CustomUser.objects.create_user(email=input("Enter email address:\t"),
                                              password=input("Set password:\t"),
                                              is_active=True)
        refresh = RefreshToken.for_user(user)
        return {"HTTP_AUTHORIZATION": f"Bearer {refresh.access_token}"}
    
    
    
    def test_create_account(self):
        print("-"*60,"\nTesting creaete account\n","-"*60)
        url = reverse("account_register")
        response = self.client.post(url, data={"email": input("\nEnter email address(for example: example@mail.com):\t"), 
                                               "password": input("Set password:\t"), 
                                               "password_confirm": str(uuid.uuid4)})
        print("\nCase with wrong confirm-password\n", "#"*60)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        response = self.client.post(url, data={"email": input("\nEnter email address(for example: example@mail.com):\t"), 
                                               "password": input("Set password:\t"), 
                                               "password_confirm": input("Enter password again:\t")})
        print("\nCase with correct passwords\n", "="*60)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, "Wrong email or password")
        
    def test_login_account(self):
        print("-"*60,"\nTesting login account\n","-"*60)
        url = reverse('token_obtain_pair')
        user = CustomUser.objects.create_user(email="example@mail.com", 
                                              password="qwerty12", 
                                              is_active=False)

        print("\nCase with inactive account\n", "="*70)        
        response = self.client.post(url, data={"email": "example@mail.com", 
                                               "password": "qwerty12"}, 
                                                format='json',
                                                is_valid=True)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.content)
    
        print("\nCase with active account\n", "="*70)
        user.is_active = True
        user.save()
        response = self.client.post(url, data={"email": "example@mail.com", 
                                               "password": "qwerty12"}, 
                                                format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_change_password(self):
        print("-"*60,"\nTesting change password account\n","-"*60)
        url = reverse("account_change_password")
        print("Old password:\t qwerty12")
        
        response = self.client.post(url, data={"old_password": "qwerty", 
                                               "new_password": input("Set new password:\t"), 
                                               "new_password_confirm": "wrong_password"}, 
                                                **self.example_bearer_token)
        print("\nCase with wrong password\n", "="*70)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        print("\nOld password:\tqwerty12")
        response = self.client.post(url, data={"old_password": "qwerty", 
                                               "new_password": input("Set new password:\t"), 
                                               "new_password_confirm": input("Confirm new password:\t")}, 
                                                **self.trial_bearer_token)
        print("\nCase with correct password\n", "="*70)
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Wrong password")

    def test_forgot_password(self):
        print("-"*60,"\nTesting change password code\n","-"*60)
        url = reverse("account_forgot_password")
        response = self.client.post(url, data={"email": input("Please, enter working email address:\t")}, **self.example_token)
        print("\nCase with email recovery\n", "="*70)
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Please enter working email address")
        
    def test_compele_password(self):
        print("-"*60,"\nTesting setting new password\n","-"*60)
        url = reverse("account_forgot_password")
        response = self.client.post(url, data={"email": "feelingjeez@gmail.com"}, **self.trial_bearer_token)
        
        url = reverse("account_complete_password")
        response = self.client.post(url, data={"email": "feelingjeez@gmail.com",
                                                "code": input("code: "),
                                                "new_password": input("Enter new password:\t"),
                                                "new_password_confirm": input("Enter again:\t")},
                                                **self.example_bearer_token,)
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Wrong password, enter password correctly")