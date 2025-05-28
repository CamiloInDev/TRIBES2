"""Modelos para la gestión del carrito de compras."""

from decimal import Decimal
from typing import TYPE_CHECKING, ClassVar

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

if TYPE_CHECKING:
    from django.contrib.auth import get_user_model
    User = get_user_model()


class Carrito(models.Model):
    """Modelo que representa el carrito de compras de un usuario."""

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="carritos",
    )
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        """Metadatos del modelo Carrito.

        Attributes:
            verbose_name: Nombre singular del modelo
            verbose_name_plural: Nombre plural del modelo
            ordering: Orden por defecto para las consultas

        """

        verbose_name: ClassVar[str] = _("carrito")
        verbose_name_plural: ClassVar[str] = _("carritos")
        ordering: ClassVar[list[str]] = ["-actualizado"]

    def __str__(self) -> str:
        """Representación en cadena del carrito."""
        return f"Carrito de {self.usuario.username}"

    @property
    def total(self) -> Decimal:
        """Calcula el total del carrito sumando los subtotales de los ítems.

        Returns:
            Decimal: El total del carrito

        """
        return sum(
            Decimal(str(item.subtotal))
            for item in self.items.all()
        )


class ItemCarrito(models.Model):
    """Modelo que representa un ítem en el carrito de compras."""

    carrito = models.ForeignKey(
        Carrito,
        related_name="items",
        on_delete=models.CASCADE,
    )
    producto = models.ForeignKey(
        "productos.Producto",
        on_delete=models.CASCADE,
        related_name="en_carritos",
    )
    cantidad = models.PositiveIntegerField(
        default=1,
        help_text="Cantidad de unidades del producto",
    )
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Precio unitario al momento de agregar al carrito",
    )
    descripcion = models.CharField(
        max_length=255,
        blank=True,
        help_text="Descripción adicional del producto",
    )

    class Meta:
        """Metadatos del modelo ItemCarrito.

        Attributes:
            verbose_name: Nombre singular del modelo
            verbose_name_plural: Nombre plural del modelo
            ordering: Orden por defecto para las consultas
            constraints: Restricciones de unicidad

        """

        verbose_name: ClassVar[str] = _("ítem del carrito")
        verbose_name_plural: ClassVar[str] = _("ítems del carrito")
        ordering: ClassVar[list[str]] = ["producto__nombre"]
        constraints: ClassVar[list[models.UniqueConstraint]] = [
            models.UniqueConstraint(
                fields=["carrito", "producto"],
                name="unique_producto_en_carrito",
            ),
        ]

    def __str__(self) -> str:
        """Representación en cadena del ítem del carrito."""
        return f"{self.cantidad} x {self.producto.nombre}"

    def save(self, *args: object, **kwargs: object) -> None:
        """Guarda el ítem en el carrito.

        Args:
            *args: Argumentos posicionales adicionales
            **kwargs: Argumentos de palabra clave adicionales

        """
        # Asegurarse de que el precio esté actualizado al del producto
        if not self.precio or self._state.adding:
            self.precio = self.producto.precio
        super().save(*args, **kwargs)

    @property
    def subtotal(self) -> Decimal:
        """Calcula el subtotal del ítem (precio * cantidad).

        Returns:
            Decimal: El subtotal del ítem

        """
        return Decimal(str(self.precio)) * self.cantidad
