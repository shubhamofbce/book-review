from django.conf import settings
from rest_framework.permissions import BasePermission, SAFE_METHODS


class SuperUserPermission(BasePermission):
    """
    Only Super user is allowed to make requests
    """

    def has_permission(self, request, view):
        return request.user.is_superuser