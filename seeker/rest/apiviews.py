from serializers import *
from ..models import *
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from seeker.rest.serializers import *
from seeker.rest.custompermissions import *

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer    
	permission_classes = (permissions.DjangoModelPermissions,)

class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer	
	permission_classes = (permissions.DjangoModelPermissions,)

class AlertViewSet(viewsets.ModelViewSet):
	queryset = Alert.objects.all()
	serializer_class = AlertSerializer	
	permission_classes = (permissions.DjangoModelPermissions,)

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer	
	permission_classes = (permissions.DjangoModelPermissions,)

	def perform_create(self, serializer):
		instance = serializer.save( product    = self.request.data['product'].lower(),)


	def perform_update(self, serializer):
		instance = serializer.save( product    = self.request.data['product'].lower(),)

class TemplateViewSet(viewsets.ModelViewSet):
	queryset = Template.objects.all()
	serializer_class = TemplateSerializer	
	permission_classes = (permissions.DjangoModelPermissions,)
	

class LookUpViewSet(viewsets.ModelViewSet):
	queryset = LookUp.objects.all()
	serializer_class = LookUpSerializer
	permission_classes = (IsInOwnerGroupOrReadOnly,)

	def perform_create(self, serializer):
			
		instance = serializer.save( created_by = self.request.user, 
									product    = self.request.data['product'].lower(),)
		

		# if product is not in Product model add it
		if not Product.objects.filter(product=self.request.data['product'].lower()).exists():
			p = Product(product=self.request.data['product'].lower())
			p.save()
					
	def perform_update(self, serializer):
		 
		instance = serializer.save()


		# if product is not in Product model add it
		if not Product.objects.filter(product=self.request.data['product'].lower()).exists():
			p = Product(product=self.request.data['product'].lower())
			p.save()
	