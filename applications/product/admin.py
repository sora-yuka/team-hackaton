from django.contrib import admin
from applications.product.models import Product, Image

class FileAdmin(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_num = 10

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        FileAdmin
    ]
    list_display = ['name', 'id', 'price']
    

admin.site.register(Product, ProductAdmin)