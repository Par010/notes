from rest_framework.viewsets import GenericViewSet
from .serializers import UserRegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework import mixins
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

class UserRegisterViewSet(mixins.CreateModelMixin,
                             GenericViewSet):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    # http_method_names = ['get', 'post', 'head']
# mixins.CreateModelMixin,
#                             GenericViewSet
