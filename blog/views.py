from django.shortcuts import render, redirect
from .models import Post
from app.models import Usr
from django.http import HttpResponse 
from .forms import PostForm
def announcement(request):
    return render(request, 'announcement.html')

def post_blog(request):
    if request.COOKIES.get('logged-in'):
        author = request.COOKIES.get('logged-in')
        if request.method == "POST":
            form_data = request.POST.copy()
            form_data['author'] = author
            form = PostForm(form_data)
            if form.is_valid():
                form.save()
                return redirect('blog:announcement')
            else:
                print("not valid")
                print(form.cleaned_data)
                print(form.errors)
    else: 
        print(request.COOKIES)
    

    return render(request, 'post.html')

