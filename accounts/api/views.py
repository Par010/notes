from rest_framework.viewsets import ModelViewSet
from .serializers import UserRegisterSerializer
from django.contrib.auth import get_user_model
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

class UserRegisterViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer(queryset, many=True)
    permission_classes = [AllowAny]
    # http_method_names = ['get', 'post', 'head']
