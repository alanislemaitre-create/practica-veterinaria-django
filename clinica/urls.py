from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.api_activa),

    path('api/propietarios/', views.api_propietarios),
    path('api/mascotas/', views.api_mascotas),
    path('api/mascotas/<int:pk>/', views.detalle_mascota),
    path('api/consultas/', views.api_consultas),

    path('api/token/', obtain_auth_token),
    path('api/perfil/', views.perfil),
    path('api/estadisticas/', views.estadisticas),
    path('api/sesion/', views.contador_sesion),
]
