from django.shortcuts import render, redirect, get_object_or_404
from .models import Propiedad
from django.contrib.auth import login, logout, authenticate
from .forms import RegistroForm, LoginForm, PropiedadForm
from django.contrib.auth.decorators import login_required
from .decorators import usuario_requerido

@login_required
@usuario_requerido(["admin", "agente"])
def dashboard(request):
    return render(request, "core/dashboard.html")

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
    else:
        form = RegistroForm()
    return render(request, "core/registro.html", {"form": form})

def iniciar_sesion(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Redirigir según el rol del usuario
            if user.rol == "ADMIN":
                return redirect("home_admin")  # Cambia por la vista de admin
            elif user.rol == "AGENTE":
                return redirect("home_agente")  # Cambia por la vista de agentes
            elif user.rol == "CLIENTE":
                return redirect("home_cliente")  # Cambia por la vista de clientes
            else:
                return redirect("home")  # Redirección por defecto
    
    else:
        form = LoginForm()

    return render(request, "core/login.html", {"form": form})

def cerrar_sesion(request):
    logout(request)
    return redirect("home")


@login_required
def lista_propiedades(request):
    propiedades = Propiedad.objects.all()
    return render(request, "core/lista_propiedades.html", {"propiedades": propiedades})


def home(request):
    return render(request, "core/home.html")

def catalogo(request):
    propiedades = Propiedad.objects.all()
    return render(request, "core/catalogo.html", {"propiedades": propiedades})


# Vistas Panel de Control
def home_admin(request):
    return render(request, "core/home_admin.html")
def home_agente(request):
    return render(request, "core/home_agente.html")
def home_cliente(request):
    return render(request, "core/home_cliente.html")


def panel_propiedades(request):
    propiedades = Propiedad.objects.all()
    return render(request, "core/panel.html", {"propiedades": propiedades})

def agregar_propiedad(request):
    if request.method == "POST":
        form = PropiedadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("panel_propiedades")
    else:
        form = PropiedadForm()
    return render(request, "core/agregar_propiedad.html", {"form": form})

def eliminar_propiedad(request, propiedad_id):
    propiedad = get_object_or_404(Propiedad, id=propiedad_id)
    propiedad.delete()
    return redirect("panel_propiedades")

def nosotros(request):
    return render(request, "core/nosotros.html")

def contacto(request):
    return render(request, "core/contacto.html")