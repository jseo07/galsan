from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm
from django.http import HttpResponse
from .models import Usr

# Create your views here.
def index(request):
    return render(request, 'index.html')

def logged_index(request):
    return render(request, 'logged_index.html')

# signup page
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:login')
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
                    response = redirect('app:logged_index')
                    response.set_cookie('logged-in', username)
                    return response
                else: 
                    form.add_error(None, "Invalid password.")
                    print(form.errors)
            except Usr.DoesNotExist:
                form.add_error(None, "Username does not exist.")
                print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def notlogged(request):
     return render(request, 'notlogged.html')

# logout page
def logout(request):
    response = redirect('app:home')
    response.delete_cookie('logged-in')
    return response
def agree(request):
    return render(request, 'agree.html')

def redirect_to_blog(request):
    return redirect('blog:announcement')
