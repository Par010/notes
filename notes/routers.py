from rest_framework import routers
from accounts.api.views import UserRegisterViewSet

router = routers.SimpleRouter()
router.register(r'userregister', UserRegisterViewSet)
