from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url,include
from accounts.api.views import UserLoginViewSet
from .routers import router
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/login', UserLoginViewSet.as_view(), name='login'),
    url(r'^api/', include(router.urls)),

]
