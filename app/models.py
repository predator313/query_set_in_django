from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=40)
    roll_number=models.IntegerField(unique=True,null=False)
    address=models.CharField(max_length=60)
    marks=models.IntegerField()
    res_date=models.DateField()

#lets see how we work with the two table as we work in sql
class Teacher(models.Model):
    name=models.CharField(max_length=40)
    salary=models.IntegerField()
    t_id=models.IntegerField(unique=True,null=False)
    address=models.CharField(max_length=60)
    join_date=models.DateField()

