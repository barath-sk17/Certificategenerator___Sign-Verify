from django.db import models

# Create your models here.

class CreateFile(models.Model):
    filename = models.CharField(max_length=50)
    rollnumber = models.CharField(max_length=25)

class Signature(models.Model):
    roll = models.CharField(max_length=200)
    text = models.FileField()
    public = models.FileField()
    signature = models.FileField()