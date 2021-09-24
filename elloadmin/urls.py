from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("admin.accounts.urls")),
    path('client/', include("admin.clients.urls")),
]
