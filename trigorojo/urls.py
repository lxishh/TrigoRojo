"""proyectoAnitaSol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from appCarro import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('menu/opciones', views.opciones, name='menuopciones'),
    #usuarios (django, login, logout)
    path('usuarios/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='authenticate/login.html'), name='login'),
    #usar las urls de la app usuarios
    path('usuarios/', include('usuarios.urls')),
    #usar las urls de la app productos
    path('productos/', include('productos.urls')),
    #usar las urls de la app ventas
    path('ventas/', include('ventas.urls')),
    #usar las urls de la app vendedores
    path('vendedores/', include('vendedores.urls')),
    #usar las urls de la app inventario
    path('inventario/', include('inventario.urls')),
]