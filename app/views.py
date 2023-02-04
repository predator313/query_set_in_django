from django.shortcuts import render
from .models import Student

# Create your views here.
#as we know in python each object is equivalenet to the each row
#of the db table
#so we use objects.all method to fetch all the record of the data
def fun(request):
    student_data=Student.objects.all()
    return render(request,'app/home.html',{'student_data':student_data})
