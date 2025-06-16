from rest_framework import permissions

class IsSelf(permissions.BasePermission):
 
    def has_object_permission(self, request, view, obj):
        return obj == request.user
    
class IsSuperAdmin(permissions.BasePermission):
  
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser