from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class RegistroUsuarioForm(UserCreationForm):
    email     = forms.EmailField(required=True)
    telefono  = forms.CharField(max_length=20, required=False)
    direccion = forms.CharField(max_length=255, required=False)

    class Meta:
        model  = CustomUser
        fields = ("username", "email", "telefono", "direccion", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email     = self.cleaned_data["email"]
        user.telefono  = self.cleaned_data["telefono"]
        user.direccion = self.cleaned_data["direccion"]
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "username":    "Nombre de usuario",
            "email":       "Correo electrónico",
            "telefono":    "Teléfono",
            "direccion":   "Dirección",
            "password1":   "Contraseña",
            "password2":   "Confirmar contraseña",
        }
        for field_name, placeholder in placeholders.items():
            if field_name in self.fields:
                self.fields[field_name].widget.attrs.update({
                    "class": "input-field",
                    "placeholder": placeholder,
                })

# Formulario para editar el perfil de usuario
class EditarPerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "telefono", "direccion")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Nombre de usuario'}),
            'email': forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Correo electrónico'}),
            'telefono': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Teléfono'}),
            'direccion': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Dirección'}),
        }
