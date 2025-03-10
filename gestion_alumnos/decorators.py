from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Group

def administrador_requerido(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied  # Bloquea si no está autenticado
        if not request.user.groups.filter(name='Administrador').exists():
            raise PermissionDenied  # Bloquea si no pertenece al grupo Administrador
        return view_func(request, *args, **kwargs)
    return wrapper
