from rest_framework import serializers
from applications.favorite.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    product = serializers.ReadOnlyField(source='product.name')
    
    class Meta:
        model = Favorite
        fields = '__all__'