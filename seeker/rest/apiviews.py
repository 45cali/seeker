from seeker.rest.serializers import *
from ..models import *
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, serializers, status
from seeker.rest.serializers import *
from seeker.rest.custompermissions import *
from seeker.rest.customvalidators import *
import json
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    # set product to lowercase
    def perform_create(self, serializer):
        instance = serializer.save(product=self.request.data['product'].lower(), )

    # set product to lowercase
    def perform_update(self, serializer):
        instance = serializer.save(product=self.request.data['product'].lower(), )


class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    permission_classes = (IsCreatorOrReadOnly,)


    def perform_create(self, serializer):

        # set owner to current user
        instance = serializer.save(owner=self.request.user)

class LookUpViewSet(viewsets.ModelViewSet):
    queryset = LookUp.objects.all()
    serializer_class = LookUpSerializer
    permission_classes = (IsInOwnerGroupOrReadOnly,)

    def perform_create(self, serializer):
        # set created_by to current user
        # set product to lowercase
        instance = serializer.save(created_by=self.request.user,
                                   product=self.request.data['product'].lower(), )


        # if product is not in Product model add it
        # set product to lowercase
        if not Product.objects.filter(product=self.request.data['product'].lower()).exists():
            p = Product(product=self.request.data['product'].lower())
            p.save()

    def perform_update(self, serializer):

        # set created_by to current user
        instance = serializer.save(created_by=str(self.request.user))


        # if product is not in Product model add it
        # set product to lowercase
        if not Product.objects.filter(product=self.request.data['product'].lower()).exists():
            p = Product(product=self.request.data['product'].lower())
            p.save()
