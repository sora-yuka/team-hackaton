from django.contrib import admin
from applications.feedback.models import Comment, Rating
from applications.product.models import Like

admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Rating)