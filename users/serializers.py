from rest_framework.serializers import ModelSerializer

from .models import User


class UserSerializer(ModelSerializer):
    """Serializer for User model."""

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}
