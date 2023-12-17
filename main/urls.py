from django.contrib import admin
from django.urls import path

from main.views import catalog, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', catalog),
    path('contact/', contact)
]
