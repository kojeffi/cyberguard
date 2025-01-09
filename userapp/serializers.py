from rest_framework import serializers
from django.contrib.auth.models import User

from.models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email', 'password')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        field = ['user','profile_picture','campany_code']