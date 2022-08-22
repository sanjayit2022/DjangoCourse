# I have created this file - Sanjay
'''
1. Create the website project - django-admin startproject mysite
2. Create the another app like mysite - python manage.py startapp mysite
3. Run server - python manage.py runserver

4. Store Migrations - python manage.py makemigrations mysite (Here mysite is mandatory if no migrations folder is created)
5. Apply migrations - python manage.py migrate

6. How to see the database table that we created
- Using superuser command - python manage.py createsuperuser

7. Open shell - python manage.py shell
'''
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee

def hello(request):
    params = {'name': 'Sanjay', 'location': 'Vadodara'}
    return render(request, 'index.html', params)
    # return HttpResponse("Hello, I am Sanjay")


def result(request):
    value = str(request.GET.get('text', 'Value is blank'))  # OR request.POST.get()
    ischecked = request.GET.get('ischecked', 'off')
    # return HttpResponse(f"This is about section, the passed value in caps is: <b>{value}</b>,\n The check box is:<b> {ischecked}</b>")
    if ischecked == 'on':
        params = {'text': value, 'ischecked': ischecked}
        return render(request, 'result.html', params)
    else:
        return HttpResponse("Error")


def process(request):
    email = request.POST.get('email', 'Missing value')
    password = request.POST.get('password', 'Missing value')
    confirm_password = request.POST.get('confirm_password', 'Missing value')
    params = {'email': email, "password": password, 'confirm_password': confirm_password}
    print(params)

    return render(request, 'process.html', params)


def add(request):
    return HttpResponse("The addition of two numbers (a +b ): 40")


def database(request):
    allEmployees = Employee.objects.all()
    params = {'employees': allEmployees}
    print(params)

    return render(request, 'database.html', params)

