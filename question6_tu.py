"""
Question 6:
Design REST API to accept TU Registration Number, Email Address, and Upload Project File
with following validation rules:
- Registration number, email and upload file are mandatory field
- Email address should be a proper email format
- Upload file format must include pdf, doc, docx, ppt, pptx, jpeg file format
- File size must be less than 5MB
"""

from rest_framework import serializers, viewsets
from django.db import models
import os

# Model
class ProjectRegistration(models.Model):
    reg_number = models.CharField(max_length=50)
    email = models.EmailField()
    project_file = models.FileField(upload_to='projects/')

# Serializer
class ProjectRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectRegistration
        fields = '__all__'
        # Registration number, email, and file are mandatory by default in ModelSerializer 
        # unless blank=True is set in Model.

    def validate_project_file(self, value):
        # 1. Validate File Format
        ext = os.path.splitext(value.name)[1].lower()
        valid_extensions = ['.pdf', '.doc', '.docx', '.ppt', '.pptx', '.jpeg', '.jpg']
        if ext not in valid_extensions:
            raise serializers.ValidationError("Allowed formats: pdf, doc, docx, ppt, pptx, jpeg.")

        # 2. Validate File Size (5MB)
        max_size = 5 * 1024 * 1024
        if value.size > max_size:
            raise serializers.ValidationError("File size must be less than 5MB.")

        return value

# View
class ProjectRegistrationViewSet(viewsets.ModelViewSet):
    queryset = ProjectRegistration.objects.all()
    serializer_class = ProjectRegistrationSerializer

print("Submitted by: Pranjal Poudel")
