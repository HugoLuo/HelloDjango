from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from APP3.models import Student, Grade


def index(request):



    #加载模版
    app3_index = loader.get_template('app3_index.html')

    context = {
        'student_name': "HUGO"
    }
    #渲染成html文件
    result = app3_index.render(context=context)



    return HttpResponse(result)


def getgrade(request):
    student = Student.objects.get(pk=1)
    grade = student.s_grade
    return HttpResponse("Grade: %s" % grade.g_name)


def getstudent(request):
    grade = Grade.objects.get(pk=1)
    students = grade.student_set.all()
    context = {
        "students": students
    }
    return render(request,'students_list.html',context=context)