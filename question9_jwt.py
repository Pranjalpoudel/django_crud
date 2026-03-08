"""
Question 9:
Write an API view that accepts username and password as arguments and check with student
table, if credential match, return JWT token otherwise display 'Invalid username/password'.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

# Model (Student Table)
class Student(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100) # In real apps, store hashed passwords

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            student = Student.objects.get(username=username, password=password)
            
            # Generate JWT Token
            refresh = RefreshToken.for_user(student)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
            
        except Student.DoesNotExist:
            return Response("Invalid username/password", status=status.HTTP_401_UNAUTHORIZED)
