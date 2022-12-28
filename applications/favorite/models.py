from django.db import models
from applications.product.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

class Favorite(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="favorites")
    
    def __str__(self):
        return self.product.name