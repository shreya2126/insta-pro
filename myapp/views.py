from django.shortcuts import render,render_to_response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import response
from rest_framework import status
from .models import employees
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# from .serializer import employeesSerializer
import json


@csrf_exempt
def employeeList(request):
    content = json.loads(request.body.decode('utf-8'))
    employee1=employees.objects.filter(firstname = content['username']).all()
    response = {}
    resp_array = []
    for emp in employee1:
        response['firstname'] = emp.firstname
        response['lastname'] = emp.lastname
        response['password'] = emp.password
        resp_array.append(response)   
        response = {}
    #serialize=employeesSerializer(employee1,many=True)
    return HttpResponse(json.dumps({'users':resp_array}), content_type='application/json', status=200) 
    
@csrf_exempt
def signup(request):
    content = json.loads(request.body.decode('utf-8'))
    print ('dasdasd  =>  ', content)
    emp = employees.objects.create(
        firstname = content['firstname'],
        lastname = content['lastname'],
        password = content['password'],
    )
    return HttpResponse(json.dumps(content), content_type='application/json', status=200) 
    
def signup_view(request):
    if request.method =='POST':
        form =UserCreationForm(request.POST)   
        if form.is_valid():
            form.save() 
            return redirect("article:list")
    else:
        form =UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})

def login_view(request):
    if request.method =='POST':
        form=AuthenticationForm()

    else:
        form =AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})       

def index(request):
    return render_to_response('index.html')