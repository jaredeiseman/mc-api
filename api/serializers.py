from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('city', 'state', 'zip', 'birth_date', 'user', 'id',)

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login', 'profile',)
        depth = 1