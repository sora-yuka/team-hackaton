from rest_framework import serializers

from applications.order.models import Order
from applications.order.tasks import send_confirmation_code


class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)
    
    class Meta:
        model = Order
        exclude = ["activation_code", "is_confirm"]
        
        
    def validate_number(self, number):
        if number.startswith('996') and len(number)==12:
            return number
        raise serializers.ValidationError("Please enter the phone number correctly")
    
             
    def create(self, validated_data):
        amount = validated_data['amount']
        product = validated_data['product']
        
        if amount == 0:
            raise serializers.ValidationError("Enter more than 0 pcs")
        if product.amount == 0:
            raise serializers.ValidationError("We don't have any product")
        if amount > product.amount:
            raise serializers.ValidationError(f"We have only {product.amount} pcs")
        
        order = Order.objects.create(**validated_data)
        send_confirmation_code.delay(order.owner.email, order.activation_code)
        return order