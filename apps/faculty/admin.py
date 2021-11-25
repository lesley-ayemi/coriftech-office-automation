from django.contrib import admin
from .models import Faculty
# Register your models here.

class FacultyAdmin(admin.ModelAdmin):
    filrer_horizontal = ('department', )
    list_display = ('name', 'phone_number')

admin.site.register(Faculty, FacultyAdmin)