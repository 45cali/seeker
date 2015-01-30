from serializers import *
from ..models import *
from django.contrib.auth.models import User, Group
from rest_framework import status, viewsets, permissions, filters
from seeker.rest.serializers import *

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer    

class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer	

class AlertViewSet(viewsets.ModelViewSet):
	queryset = Alert.objects.all()
	serializer_class = AlertSerializer	

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer	

	def perform_create(self, serializer):
		instance = serializer.save( product    = self.request.data['product'].lower(),)


	def perform_update(self, serializer):
		instance = serializer.save( product    = self.request.data['product'].lower(),)

class TemplateViewSet(viewsets.ModelViewSet):
	queryset = Template.objects.all()
	serializer_class = TemplateSerializer	
	

class LookUpViewSet(viewsets.ModelViewSet):
	queryset = LookUp.objects.all()
	serializer_class = LookUpSerializer

	def perform_create(self, serializer):
		
		instance = serializer.save( created_by = self.request.user, 
									product    = self.request.data['product'].lower(),)
		if not Product.objects.filter(product=self.request.data['product'].lower()).exists():
			p = Product(product=self.request.data['product'].lower())
			p.save()
						
	def perform_update(self, serializer):
		instance = serializer.save( created_by=self.request.user,)
		if not Product.objects.filter(product=self.request.data['product'].lower()).exists():
			p = Product(product=self.request.data['product'].lower())
			p.save()
