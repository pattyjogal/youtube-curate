from django.contrib.auth.models import User
from rest_framework import serializers
from api.curator.models import Video


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

