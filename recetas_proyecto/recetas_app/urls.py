from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('recetas/', views.ListaRecetas.as_view(), name='lista_recetas'),
    path('receta/<int:receta_id>/', views.detalle_receta, name='detalle_receta'),
    path('contacto/', views.contacto, name='contacto'),
    path('confirmacion-contacto/', views.confirmacion_contacto, name='confirmacion_contacto'),
]