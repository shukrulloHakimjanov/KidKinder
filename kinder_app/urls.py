from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about_page', views.about_page, name='about_page'),
    path('blog_page', views.blog_page, name='blog_page'),
    path('class_page', views.class_page, name='class_page'),
    path('contact_page', views.contact_page, name='contact_page'),
    path('gallery_page', views.gallery_page, name='gallery_page'),
    path('single_page', views.single_page, name='single_page'),
    path('team_page', views.team_page, name='team_page'),
    path('btn_blog', views.btn_blog_page, name='btn_blog'),
]
