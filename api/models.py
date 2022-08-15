from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.

class Task(models.Model):
  user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
  name = models.CharField(max_length=200, null=True)
  email = models.EmailField(max_length=200, null=True)
  age = models.CharField(max_length=200, null=True)
  city = models.CharField(max_length=200, null=True)
  models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
      
  def __str__(self):
    return self.name