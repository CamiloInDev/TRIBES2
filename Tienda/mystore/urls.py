"""URL configuration for mystore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.views.defaults import page_not_found

# Importar la vista personalizada de error 404
from tiendapp.views import custom_404

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin estándar de Django
    path('', include('tiendapp.urls')),  # Incluye las URLs de tiendapp
    path('usuarios/', include('django.contrib.auth.urls')),  # URLs de autenticación
    path('usuarios/', include('overrideuser.urls')),  # URLs personalizadas de usuarios
    path("carrito/", include("carrito.urls")),
    path("productos/", include("productos.urls")),
    # Ruta de prueba para 404
    path('test-404/', custom_404, name='test_404'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configurar el manejador de errores 404
handler404 = 'tiendapp.views.custom_404'

# En modo DEBUG, forzar el uso de la vista personalizada
if settings.DEBUG:
    # Captura todas las URLs no encontradas y usa la vista personalizada
    urlpatterns += [
        path('<path:undefined_path>/', custom_404, name='catch_all'),
    ]
    
    # Configurar para que use nuestra vista personalizada
    def page_not_found(request, exception, template_name='tiendapp/404.html'):
        return custom_404(request, exception)
        
    # Sobrescribir el manejador de errores
    handler404 = page_not_found
