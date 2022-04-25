from venv import create
from django.db import models
from django.core.validators import MaxValueValidator
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.conf import settings
from taggit.managers import TaggableManager

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    tags = TaggableManager(blank=True)
    vote = models.IntegerField(default=0)
    creation = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)


