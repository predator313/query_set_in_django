from django.shortcuts import render
from .models import Student,Teacher

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
def fun(request):
    sq=Student.objects.values_list('id','name',named=True)
    tq=Teacher.objects.values_list('id','name',named=True)
    combined_data=tq.difference(sq)
    print('sql query',combined_data.query)
    return render(request,'app/home.html',{'student_data':combined_data})