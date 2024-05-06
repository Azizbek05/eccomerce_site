from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('products/<slug>/', products, name='products'),
    path('register/', register, name='register'),
    path('single/<int:pk>/', single, name='single'),
]