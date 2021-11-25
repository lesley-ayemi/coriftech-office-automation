from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models.fields.related import ForeignKey, ManyToManyField
from apps.authentication.models import CustomUser
from courses.models import *
import uuid
# Create your models here.

class Faculty(models.Model):
    name = ForeignKey(CustomUser, verbose_name='Select A Faculty',on_delete=models.CASCADE)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    phone_number = models.PositiveIntegerField(blank=True, verbose_name='Enter Phone Number')
    birthdate = models.DateField(verbose_name='Enter Birthday', null=True)
    department = ManyToManyField(Course, blank=True)
    job_description = models.TextField(blank=True)
    is_head_faculty = models.BooleanField(default=False)
    salary = models.PositiveIntegerField(default=0)
    photo = models.ImageField(blank=True, default='default.png', verbose_name='profile image')
    is_active = models.BooleanField(default=True)
    employment_date = models.DateField(verbose_name='employed on', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name
    
class RequestLeave(models.Model):
    STATUS = (
        ('pending', 'PENDING'),
        ('granted', 'GRANTED'),
        ('rejected', 'REJECTED'),
    )
    title = models.CharField(max_length=255, verbose_name='Title')
    staff = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField()
    leave_duration = models.CharField(max_length=30, verbose_name='leave duration')
    status = models.CharField(max_length=30, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
# class LeaveReply(models.Model):
#     reply_title = models.ForeignKey(RequestLeave, on_delete=models.CASCADE)
#     reply_description = models.TextField()
    
#     def __str__(self):
#         return self.reply_title