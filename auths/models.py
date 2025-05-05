from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    SYSTEM_ADMIN = 'system_admin'
    EC_ADMIN = 'ec_admin'

    ROLE_CHOICES = [
        (SYSTEM_ADMIN, 'System Admin'),
        (EC_ADMIN, 'EC Admin'),
    ]

    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default=EC_ADMIN)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
