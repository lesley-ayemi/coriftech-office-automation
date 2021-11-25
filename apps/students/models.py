from courses.models import Course
from django.db import models

# Create your models here.
class StudentType(models.Model):
    type_name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.type_name
    
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    phone_number = models.PositiveBigIntegerField(null=True, blank=True)
    student_email = models.EmailField(unique=True, blank=True, null=True)
    course = models.ManyToManyField(Course)
    address = models.CharField(max_length=200)
    s_type = models.ForeignKey(StudentType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.student_name