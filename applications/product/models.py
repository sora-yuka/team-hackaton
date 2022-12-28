from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation

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


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveSmallIntegerField()
    content = GenericForeignKey('content_type', 'object_id')


class Product(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    descriptions = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_NAME)
    amount = models.PositiveIntegerField()
    likes = GenericRelation(Like)

    def __str__(self) -> str:
        return self.name
    

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')