from django.shortcuts import render, redirect
from .utils import get_completion
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout  

def home(request):
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.create_user(email = email,password=password,first_name = name,username=username)
        user.save()
        return redirect('/login')
    return render(request, 'register.html')
    

def user_login(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            login(request,user)
            return redirect('dashboard/')
    return render(request, 'user_login.html')
    

def dashboard(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        response = get_completion(prompt)
        print(response)
        return JsonResponse({'response': response})
    return render(request, 'dashboards.html')


def logout_user(request):
    logout(request)
    return redirect("/")
