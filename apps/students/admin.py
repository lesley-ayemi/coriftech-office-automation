from django.contrib import admin
from .models import (
    StudentType, Student
)
# Register your models here.
admin.site.register(StudentType)
admin.site.register(Student)