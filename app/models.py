from django.db import models

# Create your models here.

class Student(models.Model):
    s_name=models.CharField(max_length=20)
    s_age=models.IntegerField()
    s_score=models.IntegerField()