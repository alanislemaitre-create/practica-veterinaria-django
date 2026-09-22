from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_activa),

    path('api/propietarios/', views.api_propietarios),
    path('api/mascotas/', views.api_mascotas),
    path('api/mascotas/<int:pk>/', views.detalle_mascota),
    path('api/consultas/', views.api_consultas),
]
