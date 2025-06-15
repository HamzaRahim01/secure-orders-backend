from rest_framework import serializers
from .models import User 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','username']
        extra_kwargs = {
            'email': {'required': True, 'allow_blank': False},
            'username': {'required': False, 'allow_blank': True, 'allow_null': True},       
 }