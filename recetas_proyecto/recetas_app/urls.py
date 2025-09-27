from django.urls import path
from .views import ListaRecetas, contacto, confirmacion_contacto
# Importa rutas estáticas
from .views import carbonara, risotto, ensalada

urlpatterns = [
    # url de lista 
    path('', ListaRecetas.as_view(), name='lista_recetas'),
    
    # rutas estáticas para  receta
    path('recetas/carbonara/', carbonara, name='carbonara'),
    path('recetas/risotto/', risotto, name='risotto'),
    path('recetas/ensalada/', ensalada, name='ensalada'),

    # url Vistas de contacto 
    path('contacto/', contacto, name='contacto'),
    path('confirmacion_contacto/', confirmacion_contacto, name='confirmacion_contacto'),
]