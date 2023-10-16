from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from task_manager import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("manager.urls", namespace="manager")),
    path("__debug__/", include("debug_toolbar.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
