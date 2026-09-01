from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsModerator(BasePermission):

    # def has_permission(self, request, view):
    #     is_moderator = bool(request.user.groups.filter(name="Moderators").exists())
    #     if request.method in ["POST", "DELETE"] and is_moderator:
    #         return False
    #     return True
    #
    # def has_object_permission(self, request, view, obj):
    #     is_moderator = bool(request.user.groups.filter(name="Moderators").exists())
    #     if request.method in ["POST", "DELETE"] and is_moderator:
    #         return False
    #     return True

    def has_permission(self, request,view):
        return bool(request.user.groups.filter(name="Moderators").exists())


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False