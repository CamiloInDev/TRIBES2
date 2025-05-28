"""Modelos para productos y categorías de la tienda."""
from django.db import models


class Categoria(models.Model):
    """Modelo que representa una categoría de productos."""

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, default="")
    imagen = models.ImageField(upload_to="categorias/", blank=True, default="")

    class Meta:
        """Configuración extra para el modelo Categoria."""

        verbose_name = "categoría"
        verbose_name_plural = "categorías"

    def __str__(self) -> str:
        """Representación en texto de la categoría."""
        return self.nombre


class Producto(models.Model):
    """Modelo que representa un producto en la tienda."""

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, default="")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="productos",
    )
    stock = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to="productos/", blank=True, default="")

    class Meta:
        """Configuración extra para el modelo Producto."""

        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self) -> str:
        """Representación en texto del producto."""
        return self.nombre
