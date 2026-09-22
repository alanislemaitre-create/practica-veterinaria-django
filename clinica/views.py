from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Propietario, Mascota, ConsultaVeterinaria
from .serializers import (
    PropietarioSerializer,
    MascotaSerializer,
    ConsultaVeterinariaSerializer,
)


# Propietarios
# ------------------------------------------------------------------
@api_view(['GET', 'POST'])
def api_propietarios(request):
    if request.method == 'GET':
        propietarios = Propietario.objects.all().order_by('id')
        serializer = PropietarioSerializer(propietarios, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PropietarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Mascotas
# ------------------------------------------------------------------
@api_view(['GET', 'POST'])
def api_mascotas(request):
    if request.method == 'GET':
        mascotas = Mascota.objects.all().order_by('id')
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MascotaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def detalle_mascota(request, pk):
    try:
        mascota = Mascota.objects.get(pk=pk)
    except Mascota.DoesNotExist:
        return Response(
            {'error': 'Mascota no encontrada'},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = MascotaSerializer(mascota)
        return Response(serializer.data)

    if request.method in ['PUT', 'PATCH']:
        serializer = MascotaSerializer(
            mascota,
            data=request.data,
            partial=(request.method == 'PATCH')
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Consultas veterinarias
# ------------------------------------------------------------------
@api_view(['GET', 'POST'])
def api_consultas(request):
    if request.method == 'GET':
        consultas = ConsultaVeterinaria.objects.all().order_by('id')
        serializer = ConsultaVeterinariaSerializer(consultas, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ConsultaVeterinariaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def api_activa(request):
    return HttpResponse('API de Gestión Veterinaria activa')
