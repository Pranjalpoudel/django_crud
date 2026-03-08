"""
Question 3:
Write server side API to create and validate patient data with following rule and store given
data into 'patients' table with details (name, patient_id, mobile, gender, address, dob, doctor
name):
- Name, Mobile, Doctor Name, Gender, DOB: Required
- Mobile: 10 digit start with 98, 97 or 96
- DOB: YYYY-MM-DD format
"""

from rest_framework import serializers, viewsets
from django.db import models
from rest_framework.response import Response
import re

# Model (models.py)
class Patient(models.Model):
    name = models.CharField(max_length=100)
    patient_id = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    address = models.TextField(blank=True, null=True)
    dob = models.DateField()
    doctor_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'patients'

# Serializer (serializers.py)
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
    
    # Custom Validation for Mobile
    def validate_mobile(self, value):
        if not re.match(r'^(98|97|96)\d{8}$', value):
            raise serializers.ValidationError("Mobile must be 10 digits and start with 98, 97, or 96.")
        return value

# View (views.py)
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
