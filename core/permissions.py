from rest_framework.permissions import BasePermission


class IsOwnerCRUDEnabled(BasePermission):
    """Class to check if user is owner or not and if yes, then allow CRUD operations."""

    def has_permission(self, request, view):
        return request.user == view.get_object().user
