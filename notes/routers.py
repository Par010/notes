from rest_framework import routers
from accounts.api.views import (
    UserRegisterViewSet)
# from note.api.views import (
#
# )
router = routers.SimpleRouter()
router.register(r'register', UserRegisterViewSet)
# router.register(r'login', UserLoginViewSet.as_view())
