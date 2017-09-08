from rest_framework.viewsets import ModelViewSet
from .serializers import UserRegisterSerializer
from django.contrib.auth import get_user_model
from accounts.models import User
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

class UserRegisterViewSet(ModelViewSet):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    # http_method_names = ['get', 'post', 'head']
