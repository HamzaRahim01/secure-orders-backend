from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = ['id', 'user', 'status','created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

def validate(self, data):
    if data.get('status') not in dict(Order.STATUS_CHOICES):
        raise serializers.ValidationError("invalid status")
    return data