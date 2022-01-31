from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True,blank=True)
    address = models.CharField(max_length=200)

    class Meta:
        verbose_name = ("Custom User")
        verbose_name_plural = ("Custom Users")

    def __str__(self):
        return self.username
