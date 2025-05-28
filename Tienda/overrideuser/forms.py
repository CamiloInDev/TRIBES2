"""Formularios para la gestión de usuarios personalizados."""

from typing import ClassVar

from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class RegistroUsuarioForm(UserCreationForm):
    """Formulario para registrar un nuevo usuario personalizado."""

    email = forms.EmailField(required=True)
    telefono = forms.CharField(max_length=20, required=False)
    direccion = forms.CharField(max_length=255, required=False)

    class Meta:
        """Metainformación del formulario de registro de usuario personalizado."""

        model = CustomUser
        fields = (
            "username",
            "email",
            "telefono",
            "direccion",
            "password1",
            "password2",
        )

    def save(self, *, commit: bool = True) -> CustomUser:
        """Guarda el usuario con los datos proporcionados."""
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.telefono = self.cleaned_data["telefono"]
        user.direccion = self.cleaned_data["direccion"]
        if commit:
            user.save()
        return user

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Inicializa el formulario y agrega placeholders a los campos."""
        super().__init__(*args, **kwargs)
        placeholders = {
            "username": "Nombre de usuario",
            "email": "Correo electrónico",
            "telefono": "Teléfono",
            "direccion": "Dirección",
            "password1": "Contraseña",
            "password2": "Confirmar contraseña",
        }
        for field_name, placeholder in placeholders.items():
            if field_name in self.fields:
                self.fields[field_name].widget.attrs.update({
                    "class": "input-field",
                    "placeholder": placeholder,
                })

# Formulario para editar el perfil de usuario
class EditarPerfilUsuarioForm(forms.ModelForm):
    """Formulario para editar el perfil del usuario personalizado."""

    class Meta:
        """Metainformación del formulario de edición de usuario personalizado."""

        model = CustomUser
        fields = (
            "username",
            "email",
            "telefono",
            "direccion",
        )
        widgets: ClassVar[dict[str, object]] = {
            "username": forms.TextInput(
                attrs={"class": "input-field", "placeholder": "Nombre de usuario"},
            ),
            "email": forms.EmailInput(
                attrs={"class": "input-field", "placeholder": "Correo electrónico"},
            ),
            "telefono": forms.TextInput(
                attrs={"class": "input-field", "placeholder": "Teléfono"},
            ),
            "direccion": forms.TextInput(
                attrs={"class": "input-field", "placeholder": "Dirección"},
            ),
        }
