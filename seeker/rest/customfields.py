from rest_framework import serializers
import json


class JSONField(serializers.CharField):
    # serialized out

    def to_internal_value(self, obj):
        # print 'to_representation'


        if (type(obj) is str) or (type(obj) is unicode):
            #raise serializers.ValidationError('to internal value %s' % str(type(obj)))
            obj = unicode(obj)
            obj = str(obj)

            try:
                json.loads(obj)
                return json.loads(obj)

            except (TypeError, ValueError):
                return obj

        return obj


# deserialized in
    def to_representation(self, value):
        if (type(value) is str) or (type(value) is unicode):

            value = unicode(value)
            value = str(value)

            return json.loads(value)

        return value