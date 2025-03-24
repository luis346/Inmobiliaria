from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario, Propiedad

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ["username", "email", "password1", "password2", "rol"]

class LoginForm(AuthenticationForm):
    pass

class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = ["titulo", "descripcion", "tipo", "precio", "imagen", "direccion", "agente"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo usuarios con rol "AGENTE"
        self.fields["agente"].queryset = Usuario.objects.filter(rol="AGENTE")
