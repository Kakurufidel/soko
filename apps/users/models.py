from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.core.models import BaseModel

class User(AbstractUser):
    USER_ROLES = (
        ('customer', 'Customer'),
        ('vendor', 'Vendor'),
        ('manager', 'Manager'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=USER_ROLES, default='customer')
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
