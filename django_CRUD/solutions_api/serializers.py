# Submitted by: Pranjal Poudel
from rest_framework import serializers
from .models import Patient, UserData, ImageUpload, ProjectRegistration, Note, Student
from django.utils import timezone
import re
import os

# Q3: Patient Serializer
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
    
    def validate_mobile(self, value):
        if not re.match(r'^(98|97|96)\d{8}$', value):
            raise serializers.ValidationError("Mobile must be 10 digits and start with 98, 97, or 96.")
        return value

# Q4: UserData Serializer
class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'

    def validate_full_name(self, value):
        if len(value) > 40:
            raise serializers.ValidationError("Full name must be up to 40 characters.")
        return value

    def validate_username(self, value):
        if not re.match(r'^[a-zA-Z]+\d+$', value):
            raise serializers.ValidationError("Username must start with letters and end with numbers.")
        return value

    def validate_password(self, value):
        if len(value) <= 8:
            raise serializers.ValidationError("Password must be more than 8 characters.")
        return value

# Q5: ImageUpload Serializer
class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = '__all__'

    def validate_file(self, value):
        ext = os.path.splitext(value.name)[1].lower()
        if ext not in ['.jpg', '.jpeg', '.png', '.gif']:
            raise serializers.ValidationError("Only images (jpg, jpeg, png, gif) allowed.")
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError("File size must be less than 2MB.")
        return value

# Q6: Project Registration Serializer
class ProjectRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectRegistration
        fields = '__all__'

    def validate_project_file(self, value):
        ext = os.path.splitext(value.name)[1].lower()
        if ext not in ['.pdf', '.doc', '.docx', '.ppt', '.pptx', '.jpeg', '.jpg']:
            raise serializers.ValidationError("Invalid file format.")
        if value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError("File size must be less than 5MB.")
        return value

# Q7: Note Serializer
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

    def validate_content(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Content must be at least 10 characters long.")
        return value

# Q8: Appointment Serializer (No Model)
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
        if ext not in ['.pdf', '.doc', '.docx', '.jpg', '.jpeg', '.png']:
            raise serializers.ValidationError("Invalid format.")
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError("Size < 2MB required.")
        return value

    def validate_phone(self, value):
        if not (re.match(r'^9\d{9}$', value) or re.match(r'^01\d{7}$', value)):
            raise serializers.ValidationError("Format: 9********** or 01*******.")
        return value

    def validate_password(self, value):
        if len(value) < 8 or not re.search(r'[a-z]', value) or not re.search(r'[A-Z]', value) or not re.search(r'[0-9]', value) or not re.search(r'[@#$%^&+=!]', value):
            raise serializers.ValidationError("Password must be 8+ chars and contain upper, lower, digit, and symbol.")
        return value

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return data
