from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("acerca-de", views.acerca_de, name='acerca_de'),
    path('animales', views.animales, name='animales'),
    path('animales/<int:id_animal>', views.animalito, name='animal_p'),
    path('nuevo_animal', views.nuevo_animal, name= 'nuevo_animal'),
    path('clientes', views.clientes, name='clientes'),
    path('clientes/<int:DNI_cliente>', views.cliente, name='cliente_p'),
    path('nuevo_cliente', views.nuevo_cliente, name= 'nuevo_cliente'),
    path('modificar_cliente/<int:pk>', views.modificar_cliente, name='modificar_cliente'),
    path('eliminar_cliente/<int:pk>', views.eliminar_cliente, name='eliminar_cliente'),
    path('modificar_animal/<int:pk>', views.modificar_animal, name='modificar_animal'),
    path('eliminar_animal/<int:pk>', views.eliminar_animal, name='eliminar_animal')
]