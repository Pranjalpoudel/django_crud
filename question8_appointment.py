"""
Question 8:
Create a REST API to accept Name, gender, hobbies, appointment date & time, country,
resume, Email, password and confirm Password. Write server side code to perform form
validation. All fields are required. Appointment date cannot be in past. Resume should be either
pdf, ms-word or image. File size should be less than 2MB. Email should be valid. Phone number
should be valid ( 9********** or 01******* ). Password must be at least 8 character long with at
least one lowercase, uppercase, number and symbol. Password and confirm password should
match.
"""

from rest_framework import serializers, viewsets
from django.utils import timezone
import re
import os

class AppointmentSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    gender = serializers.CharField(required=True)
    hobbies = serializers.CharField(required=True)
    appointment_date = serializers.DateTimeField(required=True)
    country = serializers.CharField(required=True)
    resume = serializers.FileField(required=True)
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    def validate_appointment_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Appointment date cannot be in the past.")
        return value

    def validate_resume(self, value):
        ext = os.path.splitext(value.name)[1].lower()
        valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.jpeg', '.png']
        if ext not in valid_extensions:
            raise serializers.ValidationError("Formats: pdf, ms-word or image.")
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError("Size must be less than 2MB.")
        return value

    def validate_phone(self, value):
        # 9********** or 01*******
        if not (re.match(r'^9\d{9}$', value) or re.match(r'^01\d{7}$', value)):
            raise serializers.ValidationError("Invalid phone number format.")
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("At least 8 characters.")
        if not re.search(r'[a-z]', value):
            raise serializers.ValidationError("Must have lowercase.")
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError("Must have uppercase.")
        if not re.search(r'[0-9]', value):
            raise serializers.ValidationError("Must have number.")
        if not re.search(r'[@#$%^&+=!]', value):
            raise serializers.ValidationError("Must have symbol.")
        return value

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return data

# Note: View would involve serializer.is_valid() and saving data.

print("Submitted by: Pranjal Poudel")
