"""
URL configuration for Pokecore project.

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
from django.urls import path
from Pokefind.views import search_pokemon 
from django.http import HttpResponse
from fast_api.main import app as fast_api
from django.core.asgi import get_asgi_application
from fastapi.middleware.wsgi import WSGIMiddleware

fastapi_middleware = WSGIMiddleware(get_asgi_application())

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',search_pokemon, name='pokemon-search'),
    path('api/', fastapi_middleware),
]
async def index(request):
    return HttpResponse("Welcome to PokeFind!")