from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import CustomUser

User = get_user_model()  # Get the custom User model

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom JWT Serializer to include additional user details in the token response.
    """
    def validate(self, attrs):
        data = super().validate(attrs)  # Get default token data
        data['email'] = self.user.email
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        data['organization'] = self.user.organization
        return data

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'first_name', 'last_name']  # Remove 'username'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving user profile information.
    """
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']
