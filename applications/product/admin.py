from django.contrib import admin
from applications.product.models import Product, Image

class FileAdmin(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_num = 10

class PostAdmin(admin.ModelAdmin):
    inlines = [
        FileAdmin
    ]
    list_display = ['id', 'title', 'product_count_like']
    

admin.site.register(Product)