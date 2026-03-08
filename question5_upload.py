"""
Question 5:
Write a Django REST API to upload a file and validate:
- File extension (only allow image files: jpg, jpeg, png, gif)
- File size (must be less than 2MB)
"""

from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from django.db import models
import os

# Model
class ImageUpload(models.Model):
    file = models.FileField(upload_to='uploads/')

# Serializer
class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = ['file']

    def validate_file(self, value):
        # 1. Validate Extension
        ext = os.path.splitext(value.name)[1].lower()
        valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
        if ext not in valid_extensions:
            raise serializers.ValidationError("Only image files (jpg, jpeg, png, gif) are allowed.")

        # 2. Validate Size (2MB = 2 * 1024 * 1024 bytes)
        max_size = 2 * 1024 * 1024
        if value.size > max_size:
            raise serializers.ValidationError("File size must be less than 2MB.")

        return value

# View
class ImageUploadViewSet(viewsets.ModelViewSet):
    queryset = ImageUpload.objects.all()
    serializer_class = ImageUploadSerializer
