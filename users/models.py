from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CustomUser(AbstractUser):
    
    is_tenant = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} (Tenant: {self.is_tenant}, Manager: {self.is_manager})"


class AdminUser(models.Model):
    username = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    

    def __str__(self):
        return self.username.username