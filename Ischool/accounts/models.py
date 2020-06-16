from django.db import models
from django.utils import timezone as datetime
from django import forms

# Create your models here.

class course (models.Model):
    course_name = models.CharField(max_length=100,blank=False)
    course_number = models.CharField(max_length=100, blank=False, unique=True)
    fscore = models.IntegerField(max_length=2, blank=True)
    sscore = models.IntegerField(max_length=2, blank=True)
    cscore = models.IntegerField(max_length=2, blank=True)



class Myclas (models.Model):
    class_number = models.CharField(max_length=10, blank=False,unique=True)
    class_name = models.CharField(max_length=100,blank=False)

class teacher(models.Model):
    STATUS = (
        ('t','معلم'),
    )
    status = models.CharField(max_length=1, choices=STATUS,
                              blank=True
                              , default='t'
                              , help_text='نوع')
    date_registered = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=True, unique=True)
    user_name = models.CharField(max_length=9, blank=False,unique=True)
    password = models.CharField(max_length=32, blank=True)
    field = models.CharField(max_length=100, blank=True)
    courses = models.ManyToManyField(course)
    isactive = models.BooleanField(default=False)
    myclass = models.ManyToManyField(Myclas)
    isactive = models.BooleanField(default=False)

class student(models.Model):
    STATUS = (
        ('s','دانش آموز'),
    )
    status = models.CharField(max_length=1, choices=STATUS,
                              blank=True
                              , default='s'
                              , help_text='نوع')
    date_registered = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=True)
    user_name = models.CharField(max_length=9,blank=False, unique=True)
    password = models.CharField(max_length=32, blank=True)
    Grade = models.CharField(max_length=100, blank=True)
    taken_courses= models.ManyToManyField(course)
    my_parent = models.CharField(max_length=30,blank=False,unique=True)
    teachers = models.ManyToManyField(teacher)
    isactive = models.BooleanField(default=False)
    myclass = models.ForeignKey(Myclas, on_delete=models.CASCADE,default='0')
    rc = models.IntegerField(max_length=2, blank=True,default=1)
    rf = models.IntegerField(max_length=2, blank=True,default=1)
    rs = models.IntegerField(max_length=2, blank=True,default=1)
    phc = models.IntegerField(max_length=2, blank=True,default=1)
    phf = models.IntegerField(max_length=2, blank=True,default=1)
    phs = models.IntegerField(max_length=2, blank=True,default=1)
    chc = models.IntegerField(max_length=2, blank=True,default=1)
    chf = models.IntegerField(max_length=2, blank=True,default=1)
    chs = models.IntegerField(max_length=2, blank=True,default=1)

class deadline(models.Model):
    rday = models.IntegerField(max_length=2, blank=True,null = False ,default=2)
    rhour = models.IntegerField(max_length=2, blank=True,null = False ,default=2)
    
    phday = models.IntegerField(max_length=2, blank=True,null = False ,default=2)
    phhour = models.IntegerField(max_length=2, blank=True,null = False ,default=2)
    
    chday = models.IntegerField(max_length=2, blank=True,null = False ,default=2)
    chhour = models.IntegerField(max_length=2, blank=True,null = False ,default=2)
    


    







        
