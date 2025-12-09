from django.http import HttpResponseForbidden
from functools import wraps

def rol_requerido(rol_requerido):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):

            # ✅ SI ES SUPERUSER → ACCESO TOTAL
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)

            # ❌ SI NO TIENE PERFIL USUARIO → BLOQUEO
            if not hasattr(request.user, 'usuario'):
                return HttpResponseForbidden("No tienes un perfil de usuario asociado.")

            # ❌ SI EL ROL NO COINCIDE → BLOQUEO
            if request.user.usuario.rol != rol_requerido:
                return HttpResponseForbidden("No tienes permiso para acceder a esta página.")

            return view_func(request, *args, **kwargs)

        return _wrapped_view
    return decorator
