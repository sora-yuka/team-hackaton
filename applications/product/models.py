

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

CATEGORY_NAME = (
    ('Acessories', 'Acessories'),
    ('Electronics', 'Electronics'),
    ('Entertainment', 'Entertainment'),
    ('Clothes', 'Clothes'),
    ('Products', 'Products'),
    ('Education', 'Education'),
    ('Appliances', 'Appliances'),
    ('Sports', 'Sports'),
    ('Gadgets', 'Gadgets'),
    ('Stationery', 'Stationery'),
    ('Other', 'Other')
)

    
class Product(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    descriptions = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_NAME)
    amount = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return self.name
    
    
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')