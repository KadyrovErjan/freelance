from rest_framework import permissions

class UserEdit(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.id == request.user.id:
            return True
        return False

class CheckClient(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'client':
            return True
        return False

class CheckOfferEdit(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.freelancer == request.user:
            return True
        return False

class CheckProjectEdit(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.client == request.user:
            return True
        return False


class MethodCheck(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.client

