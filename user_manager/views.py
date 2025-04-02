import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from user_manager.models import ResUsers

@csrf_exempt
def get_users(request):
    if request.method == "GET":
        users = ResUsers.objects.all()
        return JsonResponse({'users': list(users.values())}, status=200)

def get_user(request, pk):
    if request.method == "GET":
        try:
            # Buscar el usuario por su clave primaria
            user = ResUsers.objects.get(pk=pk)
            # Devolver la información del usuario como JSON
            return JsonResponse({'user': {
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }}, status=200)
        except ResUsers.DoesNotExist:
            # Manejar el error si el usuario no existe
            return JsonResponse({'error': 'User not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def post_user(request):
    if request.method == "POST":
        try:
            json_body = json.loads(request.body.decode("utf-8"))

            # Ensure required fields are present
            required_fields = ['email', 'password', 'first_name', 'last_name']
            if not all(field in json_body for field in required_fields):
                return JsonResponse({'error': 'Missing required fields'}, status=400)

            email = json_body["email"]

            # Check if email already exists
            if ResUsers.objects.filter(email=email).exists():
                return JsonResponse({'error': 'Email already exists'}, status=400)

            # Create user instance
            user = ResUsers(**json_body)
            user.send()

            return JsonResponse({'message': 'User created successfully'}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        except IntegrityError:
            return JsonResponse({'error': 'Email already exists (IntegrityError)'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def update_user(request, pk):
    if request.method == "PATCH":
        try:
            # Buscar el usuario por su clave primaria
            user = ResUsers.objects.get(pk=pk)

            # Leer y cargar el cuerpo JSON de la solicitud
            json_body = json.loads(request.body.decode("utf-8"))

            # Actualizar las propiedades del usuario con los valores proporcionados
            for key, value in json_body.items():
                if hasattr(user, key):  # Solo actualizar si el atributo existe en el modelo
                    setattr(user, key, value)

            # Guardar los cambios en la base de datos
            user.save()

            # Respuesta de éxito
            return JsonResponse({'message': 'User updated successfully'}, status=200)

        except ResUsers.DoesNotExist:
            # Manejar el error si el usuario no existe
            return JsonResponse({'error': 'User not found'}, status=404)

        except json.JSONDecodeError:
            # Manejar errores de formato JSON
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

@csrf_exempt
def delete_user(request, pk):
    if request.method == "DELETE":
        try:
            # Buscar el usuario por su clave primaria
            user = ResUsers.objects.get(pk=pk)
            # Eliminar el usuario
            user.delete()
            # Respuesta de éxito
            return JsonResponse({'message': 'User deleted successfully'}, status=200)
        except ResUsers.DoesNotExist:
            # Manejar el error si el usuario no existe
            return JsonResponse({'error': 'User not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def login(request):
    return render(request, 'login.html')




