from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Propietario, Mascota, ConsultaVeterinaria
from .serializers import MascotaSerializer, ConsultaVeterinariaSerializer


class MascotaSerializerTest(APITestCase):
    def setUp(self):
        self.propietario = Propietario.objects.create(
            identificacion='1-1111-1111',
            nombre='Propietario de prueba',
        )

    def test_peso_cero_invalido(self):
        data = {
            'nombre': 'MascotaPrueba',
            'especie': 'Perro',
            'raza': 'Mestizo',
            'fecha_nacimiento': '2022-01-01',
            'peso': 0,
            'activo': True,
            'propietario': self.propietario.id,
        }
        serializer = MascotaSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('peso', serializer.errors)


class ConsultaSerializerTest(APITestCase):
    def setUp(self):
        propietario = Propietario.objects.create(
            identificacion='2-2222-2222',
            nombre='Otro propietario',
        )
        self.mascota = Mascota.objects.create(
            nombre='Mascota de prueba',
            especie='Gato',
            raza='Mestizo',
            fecha_nacimiento='2021-01-01',
            peso=5,
            activo=True,
            propietario=propietario,
        )

    def test_costo_negativo_invalido(self):
        data = {
            'mascota': self.mascota.id,
            'motivo': 'Consulta de prueba',
            'diagnostico': 'N/A',
            'tratamiento': 'N/A',
            'costo': -100,
        }
        serializer = ConsultaVeterinariaSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('costo', serializer.errors)


class PerfilEndpointTest(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(
            username='usuario_test', password='clave12345'
        )

    def test_perfil_sin_autenticacion_rechazado(self):
        response = self.client.get('/clinica/api/perfil/')
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

    def test_perfil_autenticado_devuelve_200(self):
        self.client.force_authenticate(user=self.usuario)
        response = self.client.get('/clinica/api/perfil/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
