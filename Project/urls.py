"""Project URL Configuration

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
# Django
from django.contrib import admin
from django.urls import include
from django.urls import path
# from store import views
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('Kategoria', views.kategorialista.as_view(), name=views.kategorialista.name),
    path('ogloszenia', views.Ogloszenielista.as_view(), name=views.Ogloszenielista.name),
    path('kategoria_lista/<int:pk>', views.Kategoriadetale.as_view(), name=views.Kategoriadetale.name),
]
