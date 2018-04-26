from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.

def student_info(request):

    #s = Student(name='ashish', age=20, std=15, section='A', address='singapore')
    #s.save()
    data = Student.objects.all()

    #return HttpResponse('<h1><center> Welcome to Django </center></h1>')
    return render(request, 'student.html', {'std_data': data})

