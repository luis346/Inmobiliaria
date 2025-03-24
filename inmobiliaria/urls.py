"""
URL configuration for inmobiliaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from core.views import home, registro, iniciar_sesion, cerrar_sesion, dashboard, lista_propiedades, catalogo, home_admin, home_agente, home_cliente, panel_propiedades, agregar_propiedad, eliminar_propiedad, contacto, nosotros   # Importa las vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("register/", registro, name="register"),
    path("login/", iniciar_sesion, name="login"),
    path("logout/", cerrar_sesion, name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
    path("properties/", lista_propiedades, name="lista_propiedades"),
    path('catalogo/', catalogo, name='catalogo'),
    path('home_admin/', home_admin, name='home_admin'),
    path('home_agente/', home_agente, name='home_agente'),
    path('home_cliente/', home_cliente, name='home_cliente'),
    path("panel/", panel_propiedades, name="panel_propiedades"),
    path("agregar/", agregar_propiedad, name="agregar_propiedad"),
    path("eliminar/<int:propiedad_id>/", eliminar_propiedad, name="eliminar_propiedad"),
    path("nosotros/", nosotros, name="nosotros"),
    path("contacto/", contacto, name="contacto"),

]
# Solo en desarrollo: sirve archivos estáticos y multimedia
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)