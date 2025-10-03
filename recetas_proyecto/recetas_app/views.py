from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Receta
from .forms import ContactoForm

# Página de inicio: muestra las últimas recetas
def inicio(request):
    recetas = Receta.objects.order_by('-id')[:6]  # últimas 6 recetas
    return render(request, 'inicio.html', {'recetas': recetas})

# Página de recetas: lista todas las recetas
class ListaRecetas(ListView):
    model = Receta
    template_name = 'lista_recetas.html'
    context_object_name = 'recetas'

# Página de detalle de receta
def detalle_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    return render(request, 'detalle_receta.html', {'receta': receta})

# Página de contacto
def contacto(request):
    mensaje = ''
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Procesar el formulario
            if form.save():
                return redirect('confirmacion_contacto')
            else:
                mensaje = 'Hubo un error al enviar tu mensaje. Por favor intenta nuevamente.'
        else:
            mensaje = 'Por favor completa todos los campos correctamente.'
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form, 'mensaje': mensaje})

def confirmacion_contacto(request):
    return render(request, 'confirmacion_contacto.html')