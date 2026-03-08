"""
Question 7:
Build a Notes CRUD API using Django Rest Framework.
"""

from rest_framework import serializers, viewsets
from django.db import models

# Model
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Serializer
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

# View
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

print("Submitted by: Pranjal Poudel")
