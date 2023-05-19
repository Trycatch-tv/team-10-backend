from rest_framework import permissions



class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.rol == 'administrador':
                return True
        return False


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.rol == 'profesor':
                return True
        return False

class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.rol == 'estudiante':
                return True
        return False
    