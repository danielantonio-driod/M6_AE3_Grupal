# Formulario contacto recetas
from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .models import Receta

class ContactoForm(forms.Form):
    nombre = forms.CharField(
        max_length=100, 
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu nombre'})
    )
    email = forms.EmailField(
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'tu@email.com'})
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Escribe tu mensaje aquí...'}), 
        label='Mensaje'
    )

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 2:
            raise forms.ValidationError('El nombre debe tener al menos 2 caracteres.')
        return nombre

    def clean_mensaje(self):
        mensaje = self.cleaned_data.get('mensaje')
        if len(mensaje) < 10:
            raise forms.ValidationError('El mensaje debe tener al menos 10 caracteres.')
        return mensaje

    def save(self):
        """
        Guarda el mensaje de contacto enviando un email y/o guardando en logs
        """
        try:
            # Enviar email (requiere configuración SMTP en settings.py)
            subject = f"Nuevo mensaje de contacto de {self.cleaned_data['nombre']}"
            message = f"""
            Nuevo mensaje de contacto recibido:

            Nombre: {self.cleaned_data['nombre']}
            Email: {self.cleaned_data['email']}
            
            Mensaje:
            {self.cleaned_data['mensaje']}
            """
            from_email = self.cleaned_data['email']
            recipient_list = [settings.DEFAULT_FROM_EMAIL] if hasattr(settings, 'DEFAULT_FROM_EMAIL') else ['admin@recetas.com']
            
            # Para desarrollo, solo imprimimos en consola
            print("="*50)
            print("NUEVO MENSAJE DE CONTACTO")
            print("="*50)
            print(f"Nombre: {self.cleaned_data['nombre']}")
            print(f"Email: {self.cleaned_data['email']}")
            print(f"Mensaje: {self.cleaned_data['mensaje']}")
            print("="*50)
            
            # Descomentar para enviar email real (requiere configuración SMTP)
            # send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            
            return True
        except Exception as e:
            print(f"Error al procesar el mensaje: {e}")
            return False