from django.db import models
class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=10, default='low')
# Create your models here.
