from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class CustomUser(AbstractBaseUser, PermissionsMixin):
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_groups',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_permissions',
        related_query_name='user',
    )
   
# to save password and username in database

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)  # You can set a different default value
    flag = models.BooleanField(default=False)


# to store uploaded images
from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploaded_images/')
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.description
