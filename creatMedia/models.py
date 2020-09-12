from django.db import models


# Create your models here.
class CreateMedia(models.Model):
    userName = models.CharField(max_length=20, help_text='Enter your name')
    image = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500, help_text='Enter give a description')
