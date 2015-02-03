from rest_framework import serializers
import json

def isList(val):

    if not type(val) is list:
        message = 'not a list'
        raise serializers.ValidationError(message)

