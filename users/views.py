from django.contrib.auth.hashers import make_password
from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer


class UserRegistrationAPIView(CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        data = request.data

        # Encrypt the password
        data['password'] = make_password(data['password'])

        return super().post(request, *args, **kwargs)
