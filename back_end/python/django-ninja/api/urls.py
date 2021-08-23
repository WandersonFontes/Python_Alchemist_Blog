
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .api import api # Api Routes


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', api.urls), # Api Routes
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


