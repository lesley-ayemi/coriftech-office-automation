from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.deletion import SET_DEFAULT
from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        # create and save a user with the given email and password
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        # create and save superuser with the given email and password
        user = self.create_user(
            email = self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_active = True 
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
        
        
        
        # extra_fields = SET_DEFAULT('is_staff', True)
        # extra_fields = SET_DEFAULT('is_superuser', True)
        # extra_fields = SET_DEFAULT('is_active', True)
        
        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError(_('Superuser must have is_staff=True.'))
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError(_('Superuser must have is_superuser=True.'))
        # return self.create_user(email, password, **extra_fields)
    
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email