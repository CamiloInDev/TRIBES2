"""Configuración de administración para usuarios personalizados."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Configuración personalizada para el modelo CustomUser en el admin."""

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "telefono",
        "is_staff",
    )
    list_filter = ("is_staff", "is_superuser", "is_active")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _( "Personal info"),
            {"fields": ("first_name", "last_name", "email", "telefono", "direccion")},
        ),
        (
            _( "Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            _( "Important dates"),
            {"fields": ("last_login", "date_joined")},
        ),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username",
                "email",
                "telefono",
                "direccion",
                "password1",
                "password2",
            ),
        }),
    )

    search_fields = (
        "username",
        "email",
        "telefono",
        "first_name",
        "last_name",
    )
    ordering = ("username",)

