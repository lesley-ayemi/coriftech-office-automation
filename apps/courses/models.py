from django.db import models
from django.urls import reverse
# Create your models here.
class Course(models.Model):
    name = models.CharField(verbose_name='enter course title', max_length=150)
    slug = models.SlugField(unique=True, max_length=200)
    price = models.FloatField(verbose_name='enter course amount')
    duration = models.CharField(verbose_name='course duration', help_text='weeks, months, year', max_length=50)
    is_availiable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse("course", args=[self.slug])
    
    def __str__(self):
        return self.name
    
    