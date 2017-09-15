from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwner(BasePermission):
    message = "You must be the owner of the object to view."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            if obj.user == request.user:  # Check permissions for read-only request
                return True
        else:
            if obj.user == request.user:  # Check permissions for write request
                return True
