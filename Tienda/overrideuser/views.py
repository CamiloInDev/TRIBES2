from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import EditarPerfilUsuarioForm, RegistroUsuarioForm


def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("Home")
    else:
        form = RegistroUsuarioForm()
    return render(request, "usuarios/registro.html", {"form": form})

def inicio_sesion_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect("Home")
    else:
        form = AuthenticationForm()

    form.fields["username"].widget.attrs.update({
        "class": "input-field",
        "placeholder": "Nombre de usuario",
    })
    form.fields["password"].widget.attrs.update({
        "class": "input-field",
        "placeholder": "Contraseña",
    })
    return render(request, "usuarios/inicio_sesion.html", {"form": form})

def cerrar_sesion_view(request):
    logout(request)
    return redirect("Home")


@login_required
def editar_perfil_view(request):
    user = request.user
    if request.method == "POST":
        form = EditarPerfilUsuarioForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect("editar_perfil")
    else:
        form = EditarPerfilUsuarioForm(instance=user)
    return render(request, "usuarios/editar_perfil.html", {"form": form})

@login_required
def eliminar_cuenta_view(request):
    user = request.user
    if request.method == "POST":
        user.delete()
        messages.success(request, "Tu cuenta ha sido eliminada.")
        return redirect("Home")
    return render(request, "usuarios/eliminar_cuenta.html")
