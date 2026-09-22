# Sistema de Gestión Veterinaria — Huellas & Salud

API REST desarrollada con Django y Django REST Framework para la
práctica integradora del curso IF0009, Desarrollo de Software IV.

## Instalación

1. Clonar el repositorio y entrar a la carpeta del proyecto
2. Crear y activar el entorno virtual:
   python -m venv .venv
   .venv\Scripts\activate

3. Instalar dependencias:
   pip install "Django>=5.2,<5.3" djangorestframework

4. Aplicar migraciones:
   python manage.py migrate

5. Crear un superusuario:
   python manage.py createsuperuser

6. Ejecutar el servidor:
   python manage.py runserver


## Endpoints

## Endpoints

### GET /clinica/
Verifica que la API está activa.
- Respuesta: texto plano
- Código: 200

### GET /clinica/api/propietarios/
Lista todos los propietarios.
- Respuesta: lista JSON
- Código: 200

### POST /clinica/api/propietarios/
Registra un propietario.
- Body: identificacion, nombre, telefono, email
- Respuesta: objeto creado
- Códigos: 201 / 400

### GET /clinica/api/mascotas/
Lista mascotas paginadas (5 por página), con filtros opcionales.
- Query params: page, especie, activas, propietario
- Respuesta: pagina_actual, total_paginas, total_mascotas, resultados
- Código: 200

### POST /clinica/api/mascotas/
Registra una mascota.
- Body: nombre, especie, raza, fecha_nacimiento, peso, activo, propietario
- Respuesta: objeto creado
- Códigos: 201 / 400

### GET /clinica/api/mascotas/<id>/
Detalle de una mascota.
- Respuesta: objeto JSON
- Códigos: 200 / 404

### PUT/PATCH /clinica/api/mascotas/<id>/
Actualiza una mascota.
- Body: campos a modificar
- Respuesta: objeto actualizado
- Códigos: 200 / 400 / 404

### DELETE /clinica/api/mascotas/<id>/
Elimina una mascota.
- Códigos: 204 / 404

### GET /clinica/api/consultas/
Lista todas las consultas.
- Respuesta: lista JSON
- Código: 200

### POST /clinica/api/consultas/
Registra una consulta.
- Body: mascota, motivo, diagnostico, tratamiento, costo
- Respuesta: objeto creado
- Códigos: 201 / 400

### POST /clinica/api/token/
Obtiene token de autenticación.
- Body: username, password
- Respuesta: token
- Códigos: 200 / 400

### GET /clinica/api/perfil/
Datos del usuario autenticado.
- Header: Authorization: Token <token>
- Respuesta: id, username, email
- Códigos: 200 / 401

### GET /clinica/api/estadisticas/
Estadísticas generales (solo administrador).
- Header: Authorization: Token <token>
- Respuesta: total_propietarios, total_mascotas, mascotas_activas, total_consultas
- Códigos: 200 / 401 / 403

### GET /clinica/api/sesion/
Contador de accesos por sesión.
- Respuesta: accesos_en_esta_sesion
- Código: 200

## Pruebas

python manage.py test

## Consultas ORM

(.venv) PS C:\Users\alani\OneDrive\Desktop\Practica_guiada_Alanis> python manage.py shell

(InteractiveConsole)
>>> from clinica.models import Mascota, Propietario, ConsultaVeterinaria
>>> Mascota.objects.all()
<QuerySet [<Mascota: Pedro>, <Mascota: Kira>, <Mascota: Rocky>, <Mascota: Luna>, <Mascota: Bolita>, <Mascota: Lola>, <Mascota: Toby>, <Mascota: Nala>]>

>>> Mascota.objects.order_by('nombre')
<QuerySet [<Mascota: Bolita>, <Mascota: Kira>, <Mascota: Lola>, <Mascota: Luna>, <Mascota: Nala>, <Mascota: Pedro>, <Mascota: Rocky>, <Mascota: Toby>]>

>>> Mascota.objects.filter(activo=True)
<QuerySet [<Mascota: Pedro>, <Mascota: Kira>, <Mascota: Rocky>, <Mascota: Luna>, <Mascota: Bolita>, <Mascota: Lola>, <Mascota: Nala>]>

>>> Mascota.objects.filter(peso__gt=10)
<QuerySet [<Mascota: Pedro>, <Mascota: Rocky>]>

>>> Mascota.objects.filter(especie='Perro')
<QuerySet [<Mascota: Rocky>, <Mascota: Toby>]>

>>> Propietario.objects.filter(nombre__icontains='ana')
<QuerySet []>

>>> propietario = Propietario.objects.get(nombre='Silvia')         
>>> propietario.mascotas.all()
<QuerySet [<Mascota: Toby>, <Mascota: Nala>]>
>>> mascota = Mascota.objects.get(nombre='Pedro')   
>>> mascota.peso = 29.0
>>> mascota.save()
>>> consulta = ConsultaVeterinaria.objects.get(mascota__nombre='Pedro')
>>> consulta.delete()
(1, {'clinica.ConsultaVeterinaria': 1})
>>>

## Reflexión final

Postman envía un POST a la URL /clinica/api/consultas/.
Django busca esa URL en urls.py y dirige la solicitud a la View.
La View recibe los datos y se los pasa al Serializer.
El Serializer realiza la validación, por ejemplo, revisa que el costo no sea negativo.
Si hay errores, la View devuelve una Response con código 400.
Si todo está correcto, el Serializer guarda los datos usando el Model.
El Model utiliza el ORM para guardar la información en la base de datos.
Finalmente, la View devuelve una Response con los datos y código 201.


