from django.shortcuts import render, redirect
from userapp.models import UserInfo, Ima1
from hashlib import sha1
from django.conf import settings
from django.http import HttpResponse
import os

# Create your views here.
list = []
list1 = []
list2 = []


def register(request):
    return render(request, 'register.html')


def register_handle(request):
    namelist = UserInfo.objects.values_list('uname')
    print(namelist)
    uname = request.POST.get('user_name')
    upwd = request.POST.get('pwd')
    upwd2 = request.POST.get('cpwd')
    uemail = request.POST.get('email')

    print(namelist)
    for i in namelist:
        list2.append(i[0])
    if uname in list2:
        return render(request, '存在.html')
    else:
        if upwd == upwd2:
            s1 = sha1()
            s1.update(upwd.encode('utf8'))
            upwd3 = s1.hexdigest()

            UserInfo.objects.create(uname=uname, upwd=upwd3, uemail=uemail)
            return render(request, 'login.html')

        else:
            return render(request, '两次不一致.html')


def dengl(request):
    return render(request, 'login.html')


def login(request):
    booklist = UserInfo.objects.values_list('uname', 'upwd')
    uname = request.POST['uname']
    upwd = request.POST['pwd']
    print(booklist)
    for i in booklist:
        list.append(i[0])
        list1.append(i[1])
    if uname in list:
        sy = list.index(uname)
        s1 = sha1()
        s1.update(upwd.encode('utf8'))
        upwd = s1.hexdigest()
        print(upwd)
        if upwd == list1[int(sy)]:
            return render(request, 'index.html')
        else:
            return render(request, '两次不一致.html')
