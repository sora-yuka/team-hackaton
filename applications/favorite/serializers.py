from rest_framework import serializers
from applications.favorite.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    
    class Meta:
        model = Favorite
        fields = '__all__'