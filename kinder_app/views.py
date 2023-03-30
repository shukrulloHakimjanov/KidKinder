from django.shortcuts import render
from .models import *

def home_page(request):
    context = {'home':'active'}
    return render(request, 'home.html',context)

def about_page(request):    
    about = About.objects.filter().first()
    context = {
        'about': about,
        'About':'active'
    }
    return render(request, 'about.html',context)


def blog_page(request):    
    blogs = Blog.objects.all()
    context={
        'blogs':blogs
    }
    return render(request, 'blog.html',context)


def class_page(request):    
    classes = Class.objects.all()
    context={
        'classes':classes
    }
    return render(request, 'class.html',context)


def contact_page(request):    
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        massage=request.POST.get('massage')
        ContactUs.objects.create(
            name=name,
            email=email,
            massage=massage,
            subject=subject,
        )
        print(name,email,massage,subject)
    return render(request, 'contact.html')


def gallery_page(request):    
    gallerys = Gallery.objects.all()
    context={
        'gallerys':gallerys
    }
    return render(request, 'gallery.html',context)


def single_page(request):    
    return render(request, 'single.html')


def team_page(request):    
    teams = Teachers.objects.all()
    parents=Teachers2.objects.all()
    context={
        'teams':teams,
        'parents':parents,
    }
    return render(request, 'team.html',context)


def btn_blog_page (request):
    blog = Blog.objects.first()
    context = {
        'blog': blog,
    }
    return render (request, 'btn_blog.html',context)