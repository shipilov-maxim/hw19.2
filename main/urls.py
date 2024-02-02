from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('', home),
    path('catalog/', catalog),
    path('contact/', contact)
]
