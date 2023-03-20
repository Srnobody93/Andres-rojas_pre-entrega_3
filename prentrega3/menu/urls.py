from django.contrib import admin
from django.urls import path, include
from menu.views import home, usuario, distribuidor, registro, buscar

urlpatterns = [ 
    path('',home, name = "index"),
    path('end_user/', usuario, name = "usuario"),
    path('distributor/',distribuidor, name = "distribuidor"),
    path('product_registration/', registro, name = "registro"),
    path('buscar_producto/', buscar, name = "buscar")
]
