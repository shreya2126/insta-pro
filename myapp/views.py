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
from .InstaScrappers import Insta_Info_Scraper
from django.template import RequestContext
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
    

def search_user_details_insta(request):
    user_name = request.GET.get('user_name')
    obj = Insta_Info_Scraper()
    data = obj.main(user_name)
    print ('data  => ',data)
    return HttpResponse(json.dumps(data), content_type='application/json', status=200) 
    

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
    # request.session['fav_color'] = 'blue'
    form =AuthenticationForm()
    print ('dsaad =>  ', request.session['fav_color'])
    return render_to_response('index.html', {'form':form})


