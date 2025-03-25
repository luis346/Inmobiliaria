from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario, Propiedad

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    rol = forms.ChoiceField(choices=Usuario.ROLES, required=True)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', 'rol']
        whitgets = {
            'rol': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2

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
