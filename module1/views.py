from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import faculty, student, contactus,datetime1
from .forms import Form1, Form2, Form3
# from django.core.mail import send_mail
from .forms import Form1
import datetime
import time
# from PIL import Image


# Create your views here.
def function1(request):
    return HttpResponse("<h1>Hello this is HomePage</h1>")


def function7(request):
    return HttpResponse("<h1>2100030123 - Mr.ABC</h1>")


def function2(request):
    return render(request, 'Homepage.html')


def function3(request):
    return render(request, 'Contact.html')


def function4(request):
    return render(request, 'Reviewdetails.html')


from .forms import *
from .models import faculty, student


# Create Employee...
def register1(request):
    if request.method == "POST":
        username1 = request.POST['username']
        username = int(username1)
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if len(username1) == 4:
            data = faculty(username=username, password=password, cpassword=cpassword)
            faculty.save(data)
            return HttpResponse("<h1>Registered fac</h1>")
        elif len(username1) == 10:
            data = student(username=username, password=password, cpassword=cpassword)
            student.save(data)
            return HttpResponse("<h1>Registered student</h1>")
        else:
            return HttpResponse("<h1>no student / fac</h1>")
    else:
        return HttpResponse("<h1>Registered123</h1>")

def login2(request):
    return render(request,'qrcode1.html')

def login1(request):
    if request.method == "POST":
        username1 = request.POST.get('username')
        username = int(username1)
        password = request.POST.get('password')
        print(username1,password)
        if len(username1) == 4:
            form = Form4()
            if faculty.objects.filter(username=username, password=password).exists():
                # return HttpResponse("Log in Success as Faculty")
                return redirect(function2)
            else:
                return HttpResponse("Invalid Faculty Details")
        if len(username1) == 10:
            form = Form5()
            if student.objects.filter(username=username, password=password).exists():
                return HttpResponse("Log in Success as Student")
            else:
                return HttpResponse("Invalid Student Details")
        if len(username1) != 10 and len(username1) != 4:
            return HttpResponse("Login Details not belongs to Student or Faculty")
    return HttpResponse("<h1>Insufficient Input - Try Again</h1>")


def function5(request):
    return render(request, 'try.html')


def function6(request):
    return render(request, 'Review1.html')


def businesssystem(request):
    return render(request, 'BusinessSystem.html')


def contactus1(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        comment = request.POST['comment']
        tosend= comment + '-------------------- This is just the copy of comment what you have posted in MMS System'
        data = contactus(firstname=firstname, lastname=lastname, email=email, comments=comment)
        data.save()
        send_mail(
            'Thank You for Contacting MMS System',
            tosend,
            'justw9090@gmail.com',
            [email],
            fail_silently=False,
        )
        return HttpResponse("<h1><center>Mail Sent</center></h1>")
        # return render(request, 'Homepage.html')
    else:
        HttpResponse("<h1>error</h1>")

def mail1(request):
    send_mail(
        'Test Mail Using Django Framework',
        'Hello Sir/Mam',
        'justw9090@gmail.com',
        ['deepak@kluniversity.in'],
        fail_silently = False,
    )
    return HttpResponse("<h1><center>Mail Sent</center></h1>")

def function8(request):
    variable1 = time.asctime(time.localtime(time.time()))
    var1 = datetime.datetime.now()
    data = datetime1(time12=variable1)
    data.save()
    return HttpResponse(variable1)

import requests
def weatherapp(request):
    if request.method == "POST":
        wh = request.POST['wh']
        api_key = '98c9fe0696484df631f05ef073b66aa4'
        user_input = wh

        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

        if weather_data.json()['cod'] == '404':
            print("No City Found")
        else:
            weather = weather_data.json()['weather'][0]['main']
            temp = round(weather_data.json()['main']['temp'])
            # °C = [(°F-32)×5] / 9
            temp1 = (((temp - 32) * 5) / 9)
            # print(type(temp))
            # print(f"The weather in {wh} is: {weather}")
            # print(f"The temperature in {user_input} is: {temp}ºF")
            # print(f"The temperature in {user_input} is: {temp1}ºC")
            return temp1
    return HttpResponse("hello")

def qrcode3(request):
    return render(request,'qrcode1.html')

import qrcode
from django.http import FileResponse
def qrcode12(request):
    if request.method == 'POST':
        sid = request.POST.get('sid')
        sname = request.POST.get('sname')
        data1 = sid+sname
        # Data to encode
        # data = "https://www.kluniversity.in/"

         # Creating an instance of QRCode class
        qr = qrcode.QRCode(version=1, box_size=30, border=5)

        # Adding data to the instance 'qr'
        qr.add_data(data1)

        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')

        img.save('static/images/KLU.png')

        img1 = open('static/images/KLU.png', 'rb')
        response = FileResponse(img1)
        return response
    # return render(request,'qrcode1.html')
    else:
        return HttpResponse("not working")
    # return HttpResponse("not working")

def alllinksfunction(request):
    return render(request,'alllinks.html')

def logout_user(request):
    logout(request)
    messages.success(request,('Youre now logged out'))
    return redirect('homepage')

def function9(request):
    return render(request, 'login2.html')



