from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password. This user is just a normal user with just base privilleges."""
        if not email:
            raise ValueError('The Email field must be set')
        # We validate the email
        email = self.normalize_email(email)
        # We create the user object
        user = self.model(email=email, **extra_fields)
        # we set the password to be the user input password that is hashed to avoid direct decoding of passwords
        user.set_password(password)
        # We save the user to the database
        user.save(using=self._db)
        # We return the user object
        return user


    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        # for a user to be a supruser or admin there some fields we have to enable to give the user extra previllages
        # 1. We make the user a staff member
        extra_fields.setdefault('is_staff', True)
        # 2. We make them admin
        extra_fields.setdefault('is_superuser', True)
        # 3. We mark them active admins
        extra_fields.setdefault('is_active', True)


        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff set to True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser set to be True.')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom defined user model"""
    first_name = models.CharField(max_length=30, null=True)
    """User's first name"""
    last_name = models.CharField(max_length=30, null=True)
    """User's last name"""
    email = models.EmailField(unique=True, null=True)
    """User's email address"""
    username = None
    """User's username which will be empty since we won't be using the field"""
    is_staff = models.BooleanField(default=False)
    """User's staff status"""
    is_active = models.BooleanField(default=True)
    """User's active status"""
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    """User's date joined"""
    last_login = models.DateTimeField(auto_now=True, null=True)
    """User's last login"""

    USERNAME_FIELD = 'email'
    # Setting the required fields to an empty array
    REQUIRED_FIELDS = []
    # Create a custom user model
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


    def __str__(self):
        return self.email.__str__()