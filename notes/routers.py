from rest_framework import routers
from accounts.api.views import (
    UserRegisterViewSet)

router = routers.SimpleRouter()
router.register(r'register', UserRegisterViewSet)
# router.register(r'login', UserLoginViewSet.as_view())
