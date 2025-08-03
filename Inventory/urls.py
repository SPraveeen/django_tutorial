from django.urls import path
from .views import *

urlpatterns = [
    path('home/',HomePage),
    path('about/',AboutPage),
    path('contact/',ContactPage),
    path('service/',ServicePage),
    path('products/add/',ProductsAdd),
    path('products/',AllProducts),
]
