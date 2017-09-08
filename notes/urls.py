from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url,include

from .routers import router
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]
