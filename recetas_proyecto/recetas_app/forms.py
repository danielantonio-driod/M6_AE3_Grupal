#formulario contacto recetas
from django import forms
from .models import Receta
class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    email = forms.EmailField(label='Correo Electrónico')
    mensaje = forms.CharField(widget=forms.Textarea, label='Mensaje')

    def save(self):
        # Aquí podrías implementar la lógica para enviar un correo electrónico
        # o guardar el mensaje en la base de datos.
        pass
        # Por ahora, solo imprimimos los datos en la consola.
        print(f"Nombre: {self.cleaned_data['nombre']}")
        print(f"Email: {self.cleaned_data['email']}")
        print(f"Mensaje: {self.cleaned_data['mensaje']}")
        # En un caso real, podrías usar Django's send_mail function.
        # from django.core.mail import send_mail
        # send_mail(
        #     f"Nuevo mensaje de {self.cleaned_data['nombre']}",
        #     self.cleaned_data['mensaje'],
        #     self.cleaned_data['email'],