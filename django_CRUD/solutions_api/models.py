# Submitted by: Pranjal Poudel
from django.db import models

# Q3: Patient Model
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

# Q4: UserData Model
class UserData(models.Model):
    full_name = models.CharField(max_length=40)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

# Q5: ImageUpload Model
class ImageUpload(models.Model):
    file = models.ImageField(upload_to='uploads/')

# Q6: ProjectRegistration Model
class ProjectRegistration(models.Model):
    reg_number = models.CharField(max_length=50)
    email = models.EmailField()
    project_file = models.FileField(upload_to='projects/')

# Q7: Note Model
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Q9: Student Model for JWT
class Student(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
