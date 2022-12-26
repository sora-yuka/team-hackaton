from rest_framework import serializers

from applications.order.models import Order
from applications.order.tasks import send_confirmation_email


class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)
    
    class Meta:
        model = Order
        fields = '__all__'
        
    def create(self, validated_data):
        amount = validated_data['amount']
        product = validated_data['product']
        if amount > product.amount:
            raise serializers.ValidationError(f'We have only {product.amount} pcs')
        if amount == 0:
            raise serializers.ValidationError('Enter more than 0 pcs')
        
        product.amount -= amount
        product.save(update_fields=['amount'])
        
        order = Order.objects.create(**validated_data)
        send_confirmation_email.delay(order.owner.email, order.activation_code, order.product.name, order.total_price)
        return 