from django.contrib import admin
from applications.feedback.models import Like, Comment, Rating

admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Rating)