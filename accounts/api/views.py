from rest_framework.viewsets import GenericViewSet
from .serializers import (
    UserRegisterSerializer,
    UserLoginSerializer
    )
from django.contrib.auth import (
    get_user_model,
    login,
    authenticate,
    logout
    )
from rest_framework import mixins
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.response import Response
# from accounts.models import User
from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
# from rest_framework.generics import(
#     ListAPIView,
#     RetrieveAPIView,
#     UpdateAPIView,
#     DestroyAPIView,
#     RetrieveUpdateAPIView,
#     CreateAPIView
#     )

User = get_user_model()

class UserRegisterViewSet(
    mixins.CreateModelMixin,
    GenericViewSet):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

class UserLoginViewSet(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
