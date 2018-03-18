from django.db import models

# Create your models here.
class Student(models.Model):
	roll_no = models.CharField(max_length=10)
	name = models.CharField(max_length=100)
	div = models.CharField(max_length=1)
	branch = models.CharField(max_length=50)
	year = models.CharField(max_length=2)