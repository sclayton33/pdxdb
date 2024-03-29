from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    # TODO: seems to POST without being logged in
    def has_object_permission(self, request, view, obj):
        """
        If user is author of Pdx model, they have full CRUD permissions.
        Otherwise only read.
        """

        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author of a post
        return obj.author == request.user
