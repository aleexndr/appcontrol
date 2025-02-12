from django.urls import path
from . import views


from .views import reiniciar_alimentos

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar_alimento/', views.registrar_alimentos, name='registrar_alimentos'),
    path('reiniciar_alimentos/', reiniciar_alimentos, name='reiniciar_alimentos'),
]