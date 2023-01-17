from django.db import models

# models.py 수정했다 -> 무족건 makemigrations -> migrate
class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    gpa = models.FloatField() #학점
    major = models.CharField(max_length=20)
