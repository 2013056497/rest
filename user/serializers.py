from rest_framework import serializers
from user.models import RestUser


class RestUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestUser
        fields = ['name', 'address', 'mobile', 'date_of_birth']
