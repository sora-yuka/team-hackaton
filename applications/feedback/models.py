# from email._header_value_parser import ContentType
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey



from django.contrib.auth import get_user_model
from django.db import models
from applications.product.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


# class Like(models.Model):
#     owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes')
#     like = models.BooleanField(default=False)
#
#     def __str__(self) -> str:
#         return f'{self.owner} - {self.like}'

class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        blank=True, null=True
    )

    def __str__(self):
        return self.owner


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveSmallIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
