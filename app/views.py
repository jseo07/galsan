from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm
from django.http import HttpResponse
from .models import Usr

# Create your views here.
def index(request):
    return render(request, 'index.html')

# signup page
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.cleaned_data)
            return HttpResponse('form not valid')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# login page
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['usrname']
            password = form.cleaned_data['password']
            try:
                verification = Usr.objects.get(usrname = username)
                if verification.password == password:
                    print(verification.password)
                    print("successful")
                    return redirect('home')
                else: 
                    form.add_error(None, "Invalid password.")
                    print(form.errors)
            except Usr.DoesNotExist:
                form.add_error(None, "Username does not exist.")
                print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def logout(request):
    return redirect('login')

def agree(request):
    return render(request, 'agree.html')
