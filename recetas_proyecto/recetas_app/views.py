from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Receta
from .forms import ContactoForm

# Esta vista se mantiene sin cambios.
class ListaRecetas(ListView):
    model = Receta
    template_name = 'lista_recetas.html'
    context_object_name = 'recetas'

# Vistas de función estáticas para cada receta
def carbonara(request):
    return render(request, 'carbonara.html')

def risotto(request):
    return render(request, 'risotto.html')

def ensalada(request):
    return render(request, 'ensalada.html')
    
# Vistas de contacto
def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            return redirect('confirmacion_contacto') 
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})
    
def confirmacion_contacto(request):
    return render(request, 'confirmacion_contacto.html')