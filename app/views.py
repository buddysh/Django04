import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Student


def index(request):
    return render(request,'index.html')


def testpage(request):
    stus=Student.objects.all().order_by('-s_score')
    name='张三'

    return render(request,'testpage.html',context={'abc':stus})


def addstu(request):
    stu=Student()
    stu.s_name='Tom'+str(random.randrange(10,100))
    stu.s_age=random.randrange(10,20)
    stu.s_score=random.randrange(0,100)
    stu.save()
    return HttpResponse('添加成功'+stu.s_name)