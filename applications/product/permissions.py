from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsProductOwnerOrReadOnly(BasePermission):
    
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.method == "POST":
            return request.user.is_authenticated or request.user.is_staff
        return request.user.is_authenticated and (request.user == obj.owner or request.user.is_staff)