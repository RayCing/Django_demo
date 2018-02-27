from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import  Grades,Students

def index(request):
    return HttpResponse("Hello")

def detail(request,num):

    return HttpResponse("detail-%s"%num)

def grades(request):
    #去模板里取数据
    gradesList = Grades.objects.all()
    #将数据传递给模板,模板渲染页面，将渲染好的页面返回给浏览器

    return render(request,'Myapp/grades.html',{"grades":gradesList})


def students(request):
    studentsList = Students.objects.all()
    return render(request,'Myapp/students.html',{"students":studentsList})

def gradesStudents(request,num):
    #获得对应班级对象
    grade = Grades.objects.get(pk=num)
    #获得班级下的所有学生对象列表
    studentsList = grade.students_set.all()
    return render(request,'Myapp/students.html',{"students":studentsList})
