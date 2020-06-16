from django import forms
from .models import student,teacher

class loginform(forms.Form):
    login = forms.CharField(label=False, required=True,widget=forms.TextInput(attrs={'placeholder':'نام کاربری', 'class': 'form-control m-input m-login__form-input--last', 'style':"font-family: vazir;"}), max_length=50)
    password = forms.CharField(label=False, required=True,widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور', 'class': 'form-control m-input m-login__form-input--last', 'style':"font-family: vazir;"}) , max_length=80)
 

class setscore(forms.Form):
    cscore = forms.CharField(label=False,required=True ,widget=forms.TextInput(attrs={'placeholder':'نمره مستمر', 'class': 'form-control col-xl-3 col-lg-3 m-input m-login__form-input--last', 'style':"font-family: vazir;"}), max_length=2)
    fscore = forms.CharField(label=False,required=True ,widget=forms.TextInput(attrs={'placeholder':'نمره نوبت اول', 'class': 'form-control  col-xl-3 col-lg-3 m-input m-login__form-input--last', 'style':"font-family: vazir;"}), max_length=2)
    sscore = forms.CharField(label=False,required=True ,widget=forms.TextInput(attrs={'placeholder':'نمره نوبت دوم', 'class': 'form-control  col-xl-3 col-lg-3 m-input m-login__form-input--last', 'style':"font-family: vazir;"}), max_length=2)

class changepassword(forms.Form):
    lpassword = forms.CharField(label=False, required=True,widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور فعلی', 'class': 'form-control m-input m-login__form-input--last', 'style':"font-family: vazir; margin-bottom: 2%;"}) , max_length=80)
    npassword = forms.CharField(label=False, required=True,widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور جدید', 'class': 'form-control m-input m-login__form-input--last', 'style':"font-family: vazir; vazir; margin-bottom: 2%;"}) , max_length=80)
    npassword2 = forms.CharField(label=False, required=True,widget=forms.PasswordInput(attrs={'placeholder':'تکرار رمز عبور جدید', 'class': 'form-control m-input m-login__form-input--last', 'style':"font-family: vazir; vazir; margin-bottom: 2%;"}) , max_length=80)

class importfile(forms.Form):
    Choises = [
        ('r' , 'ریاضی'),
        ('ph' , 'فیزیک'),
        ('ch' , 'شیمی'),
    ]
    coursename =forms.TypedChoiceField(
        required=True, label=False,
        choices=Choises,
    )
class sethomework(forms.Form):
    days = forms.CharField(label=False,required=True ,widget=forms.TextInput(attrs={'placeholder':'تعداد روز های مهلت', 'class': 'form-control col-xl-9 col-lg-9 m-input m-login__form-input--last', 'style':"font-family: vazir;"}), max_length=2)
    hours = forms.CharField(label=False,required=True ,widget=forms.TextInput(attrs={'placeholder':'تعداد ساعت های مهلت', 'class': 'form-control col-xl-9 col-lg-9 m-input m-login__form-input--last', 'style':"font-family: vazir;"}), max_length=2)
