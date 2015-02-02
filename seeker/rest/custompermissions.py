from django.contrib.auth.models import User, Group
from rest_framework import permissions
from ..models import LookUp


class IsInOwnerGroupOrReadOnly(permissions.BasePermission):
	"""
	Custom permission to only allow owners of an object to edit it.
	"""

	def has_permission(self, request, view):
		if request.method in permissions.SAFE_METHODS:
			return True

		# diable PATCH	
		if request.method == 'PATCH':
			return False

		# owner must be a Group that user is apart of 
		if 'owner' in request.data:
            		
			user = User.objects.get(username=request.user)
			is_in_group = user.groups.filter(name=request.data['owner']).exists()
            
			return 	is_in_group

		return True

	def has_object_permission(self, request, view, obj):
		"""
		Custom object permission to only allow owners of an object to edit it.
		"""
		if request.method in permissions.SAFE_METHODS:
			return True

		if obj.id:
			user = User.objects.get(username=request.user)
			current_owner_group = str(LookUp.objects.get(pk=obj.id).owner)
			is_in_group = user.groups.filter(name=current_owner_group).exists()

			# only users of current owner group can edit it
			return is_in_group

		return False
		

class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # only owner has rw permissions
        return unicode(obj.owner) == unicode(request.user)