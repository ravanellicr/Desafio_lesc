"""desafio_lesc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from .views import list_atividades,create_atividades,update_atividades,delete_atividades

urlpatterns = [
    path('', list_atividades, name = 'list_atividades'),
    path('new', create_atividades, name = 'create_atividades'),
    path('update/int:id', update_atividades, name = 'update_atividades'),
    path('delete/int:id', delete_atividades, name = 'delete_atividades'),
]
