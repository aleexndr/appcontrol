from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar_alimento/', views.registrar_alimentos, name='registrar_alimentos'),
    
]