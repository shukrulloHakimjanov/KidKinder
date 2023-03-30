from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import datetime
class About(models.Model):

    img = models.ImageField(upload_to='about/')
    title = models.CharField(max_length=250)
    description = RichTextUploadingField()

    def __str__(self):
        return f"{self.title} - {self.description}"


class Class(models.Model):
    Card = (
        ('Art', 'Art'),
        ('Music', 'Music'),
        ('reading', 'reading'),
    )
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True, null=True)
    img = models.ImageField(upload_to='')
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=150)
    age = models.CharField(max_length=200)
    groups = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    money = models.CharField(max_length=200)
    card = models.CharField(max_length=50,choices=Card)

    def __str__(self):
        return f'{self.title}'

class Teachers(models.Model):
    img = models.ImageField(upload_to='')
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=150)
    tw = models.CharField(max_length=255, null=True,blank=True)
    fac = models.CharField(max_length=255, null=True,blank=True)
    In = models.CharField(max_length=255, null=True,blank=True)

    def __str__(self):
        return self.title

class Teachers2(models.Model):
    img = models.ImageField(upload_to='')
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=150)
    profession=models.CharField(max_length=150)
    def __str__(self):
        return f'{self.title}'



class Gallery(models.Model):
    img = models.ImageField(upload_to='')



class Blog(models.Model):
    img = models.ImageField(upload_to='')
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=150)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ContactUs(models.Model):
    email = models.EmailField(max_length=250)
    name = models.CharField(max_length=250)
    subject = models.CharField(max_length=255)
    massage = models.TextField(max_length=255)

    





