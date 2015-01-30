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
		fields = ('url', 'name')	

class AlertSerializer(serializers.ModelSerializer):
	class Meta:
		model = Alert
		fields = ('url','alert')

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('url','product')		

class TemplateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Template
		fields = ('url','name', 'description', 'alert_set')

class LookUpSerializer(serializers.ModelSerializer):
	

	class Meta:
		model = LookUp
		fields = ('url',
				'pattern',
				'product',
				'created_by',
				'owner',
				'alert_set')


