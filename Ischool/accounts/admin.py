from django.contrib import admin
from .models import student, course, teacher,Myclas,deadline
# Register your models here.


class studentadmin(admin.ModelAdmin):
    list_display = ('status','first_name','last_name','user_name','password','Grade','my_parent')
    prepopulated_fields = {'password': ('user_name',)}
    list_filter = ('user_name','last_name','Grade')
    search_fields = ('user_name', 'last_name', 'first_name')
    ordering = ['last_name','user_name']
admin.site.register(student, studentadmin)

class courseadmin(admin.ModelAdmin):
    list_display = ('course_name','course_number')
    list_filter = ('course_name','course_number')
    search_fields = ('course_name', 'course_number')
    ordering = ['course_number','course_name']
admin.site.register(course, courseadmin)

class taecheradmin(admin.ModelAdmin):
    list_display = ('status','first_name','last_name','user_name','password','field')
    prepopulated_fields = {'password': ('user_name',)}
    list_filter = ('user_name','last_name','field')
    search_fields = ('user_name', 'last_name', 'first_name')
    ordering = ['user_name','last_name']
admin.site.register(teacher,taecheradmin )

class classadmin(admin.ModelAdmin):
    list_display = ('class_name','class_number')
    ordering = ['class_number']
    search_fields = ('class_name',)
admin.site.register(Myclas,classadmin)

# class deadlineadmin(admin.ModelAdmin):
#     list_display = ('rday','rhour','phday','phhour','chday','chhour')
# admin.site.register(deadline,deadlineadmin)