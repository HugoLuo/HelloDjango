from django.shortcuts import render
from django.http import HttpResponse

from APP.models import Student

import random

# Create your views here.


# one type Response
def hello(request):
    return HttpResponse("Hello")

# two type Response
def haha(request):
    return HttpResponse("<h1><center>h哈哈</center></h1>")

# three type Response  it will access App2 templates html file(App2 urls.py will include to primary urls)
def index(request):
    return render(request,"index.html")


# three type Response  it will access Project templates html file(Project setting file will setting Template part's DIRS path )
def home(request):
    return render(request,"home.html")

def add_stu(request):
    student = Student()
#    student.s_name="Cici"
    student.s_name="student%d" % random.randrange(100)
    student.save()
    return HttpResponse("have add the student %s" %(student.s_name))


def list_stu(request):
    studtents = Student.objects.all()
#    for studtent in studtents:
#        print(studtent.s_name)
#    return HttpResponse("all the students as below")
    context = {
            "hobby": "Play football",
            "students": studtents
    }
    return render(request,"list_students.html",context=context)


def del_stu(request):
    student =Student.objects.get(pk=5)
    student.delete()
    return HttpResponse("the student %s have delete" % student.s_name)

def update_stu(request):
    student=Student.objects.get(pk=6)
    student.s_name = "GiGi"
    student.save()
    return HttpResponse("the student %s have updated" % student.s_name)