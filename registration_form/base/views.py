from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import SignupForm

# Create your views here.

def homePage(request):
    return render(request, 'index.html')

def loginPage(request):

    form = SignupForm()
    if request.method == 'POST':
        if request.POST.get('submit') == 'Login':
            username = request.POST.get('username').lower()
            password = request.POST.get('password')

            try:
                user = User.objects.get(username=username)
            except:
                return HttpResponse("Invalid Username!!")
        
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse("Invalid Username or Password!!")
            
        elif request.POST.get('submit') == 'Signup':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse("An error occured during sign up!!")
    
    

    context = {'form':form}
    return render(request, 'base/register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')

# def signupPage(request):
#     form = UserCreationForm()

#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()
#             login(request, user)
#             return redirect('home')
#         else:
#             return HttpResponse("An error occured during sign up!!")

#     context = {'form': form}
#     return render(request, 'base/register.html', context)