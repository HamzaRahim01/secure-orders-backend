from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']
        extra_kwargs = {
            'email': {'required': True, 'allow_blank': False},
            'username': {'required': False, 'allow_blank': True, 'allow_null': True},
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.pop('password'))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)