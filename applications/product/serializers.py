from rest_framework import serializers
from applications.product.models import Product, Image
from django.db.models import Avg


class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Image
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)
    file_image = ImageSerializer(many=True, read_only=True)
    
    
    class Meta:
        model = Product
        fields = '__all__'
        
    def create(self, validated_data):
        request = self.context.get('request')
        product = Product.objects.create(**validated_data)
        files = request.FILES
        list_images = []
        
        for image in files.getlist('images'):
            list_images.append(Image(product=product, image=image))
        Image.objects.bulk_create(list_images)
        return product
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['likes'] = instance.likes.filter(object_id=True).count()
        rep['rating'] = instance.ratings.all().aggregate(Avg('rating'))['rating__avg']
        return rep