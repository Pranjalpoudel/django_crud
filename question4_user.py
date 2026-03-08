"""
Question 4:
Design REST API to store user data and perform following validation rules:
- Length of Full name up to 40 characters
- Email address must be valid email address
- Username must start with string and followed by number
- Password length must be more than 8 characters
"""

from rest_framework import serializers, viewsets
from django.db import models
import re

# Model
class UserData(models.Model):
    full_name = models.CharField(max_length=40)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

# Serializer
class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'

    def validate_full_name(self, value):
        if len(value) > 40:
            raise serializers.ValidationError("Full name must be up to 40 characters.")
        return value

    def validate_username(self, value):
        # Starts with string (alpha) and followed by number (digits)
        if not re.match(r'^[a-zA-Z]+\d+$', value):
            raise serializers.ValidationError("Username must start with letters and end with numbers.")
        return value

    def validate_password(self, value):
        if len(value) <= 8:
            raise serializers.ValidationError("Password must be more than 8 characters.")
        return value

# View
class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
