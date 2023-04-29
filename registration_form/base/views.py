from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
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
                messages.error(request, 'Invalid Username!!')
                return redirect('login')
        
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid Username or Password!!')
                return redirect('login')
            
        elif request.POST.get('submit') == 'Signup':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                login(request, user)
                return redirect('home')
            else:
                # messages.error(request, "An error occured during sign up!!")
                messages.error(request, "Password can’t be too similar to your other personal information.")
                messages.error(request, "Password must contain at least 8 characters.")
                messages.error(request, "Password can’t be a commonly used password.")
                messages.error(request, "Password can’t be entirely numeric.")
                return redirect('login')
    

    context = {'form':form}
    return render(request, 'base/register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')
