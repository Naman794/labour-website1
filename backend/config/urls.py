from django.contrib import admin
from django.urls import path, include
from core.views import health_check

urlpatterns = [
    path("admin/", admin.site.urls),
    path("healthz", health_check, name="healthz"),
    path("auth/", include("accounts.urls")),
    path("api/", include("core.urls")),
]
