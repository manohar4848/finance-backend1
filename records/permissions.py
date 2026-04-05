from rest_framework.permissions import BasePermission

class RecordPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        # Must be logged in
        if not user or not user.is_authenticated:
            return False

        # Viewer → only GET
        if user.role == 'viewer':
            return request.method == 'GET'

        # Analyst → GET + dashboard access
        if user.role == 'analyst':
            return request.method == 'GET'

        # Admin → full access
        if user.role == 'admin':
            return True

        return False