from django.shortcuts import render
from .models import Student,Teacher
from django.db.models import Q
#here we import which is used for the encapsulation
#means the combining purpose  for two or more object

# Create your views here.
#as we know in python each object is equivalenet to the each row
#of the db table
#so we use objects.all method to fetch all the record of the data
# def fun(request):
#     student_data=Student.objects.all()
#     print('sql query',student_data.query)
#     return render(request,'app/home.html',{'student_data':student_data})
    #we also pass the two method of filter and exclude
    #same as the sql in and notin method
    #  
#we can use ours various django command which is
#similar to the sql database
#more familar to the sql lite db
# def fun(request):
#     sq=Student.objects.values_list('id','name',named=True)
#     tq=Teacher.objects.values_list('id','name',named=True)
#     combined_data=tq.difference(sq)
#     print('sql query',combined_data.query)
#     return render(request,'app/home.html',{'student_data':combined_data})
# def fun(request):
#     student_data=Student.objects.filter(marks__lt=90)
#     print('sql query',student_data.query)
#     return render(request,'app/home.html',{'student_data':student_data})

def fun(request):
    student_data=Student.objects.filter(Q(id=4)|
    Q(id=2))
    print('sql query',student_data.query)
    return render(request,'app/home.html',{'student_data':student_data})