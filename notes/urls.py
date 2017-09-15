from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url,include
from accounts.api.views import UserLoginViewSet
from .routers import router
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/login', UserLoginViewSet.as_view(), name='login'),
    url(r'^api/', include(router.urls)),
    url(r'^api/auth/token/', obtain_jwt_token),   #get jwt token

]
