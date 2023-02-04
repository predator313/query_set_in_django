from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=40)
    roll_number=models.IntegerField(unique=True,null=False)
    address=models.CharField(max_length=60)
    marks=models.IntegerField()
    res_date=models.DateField()
