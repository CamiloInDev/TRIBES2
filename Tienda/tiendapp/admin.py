from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.utils.translation import gettext_lazy as _

# Usar el admin de Django por defecto
admin.site.site_header = 'Administración de Tribes'
admin.site.site_title = 'Sitio de administración de Tribes'
admin.site.index_title = 'Panel de control'
