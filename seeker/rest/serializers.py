from django.contrib.auth.models import User, Group
from ..models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'is_staff', 'groups')
		
class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'id', 'name')	

class AlertSerializer(serializers.ModelSerializer):
	class Meta:
		model = Alert
		fields = ('url', 'id', 'alert')

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('url', 'id', 'product')		

class TemplateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Template
		fields = ('url', 'id', 'name', 'description', 'alert_set', 'owner')

class LookUpSerializer(serializers.ModelSerializer):
	

	class Meta:
		model = LookUp
		fields = ('url',
				'id',
				'pattern',
				'product',
				'created_by',
				'owner',
				'alert_set')


