from django.db import models


# Create your models here.
class Quiz(models.Model):
    name=models.CharField(max_length=100)
    score=models.IntegerField()
    time=models.TimeField()