from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Course
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration')
    prepopulated_fields = {"slug": ("name",)}
    
admin.site.register(Course, CourseAdmin)