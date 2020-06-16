from django.shortcuts import render,redirect, get_object_or_404
from .models import teacher, course, student, Myclas, deadline
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.postgres.search import SearchVector
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import loginform,setscore,changepassword,importfile,sethomework
from django.http import HttpResponse
from django.core.files.storage import  FileSystemStorage










def login(request):
    text = 0 
    text2 = 1
    text4 =' '
    text3 =0
    if request.method == 'POST':
        form = loginform(request.POST,request.FILES)
        if form.is_valid():
            text = form.cleaned_data['login']
            text2 = form.cleaned_data['password']
            if  student.objects.filter(user_name = text) and student.objects.filter(password = text2):
                text3 = student.objects.filter(user_name=text)[0]
                act = text3.isactive
                act = True
                text3.isactive = act
                text3.save()
                userid = text
                return redirect('student/'+userid+'/')
            elif teacher.objects.filter(user_name = text) and teacher.objects.filter(password = text2):
                text3 = teacher.objects.filter(user_name=text)[0]
                act = text3.isactive
                act = True
                text3.isactive = act
                text3.save()
                userid = text
                return redirect('teacher/'+userid+'/')
            elif student.objects.filter(my_parent = text) and student.objects.filter(my_parent = text2):
                text3 = student.objects.filter(my_parent=text)[0]
                act = text3.isactive
                act = True
                text3.isactive = act
                text3.save()
                userid = text
                return redirect('parent/'+userid+'/')
            else:
                text4 = 'اطلاعات وارد شده اشتباه است! دوباره تلاش کنید.'


    else:
        form =loginform()
        
    context = {
        'form': form,
        'text': text,
        'text2': text2,
        'text4': text4,
        'text3': text3,
    }
    return render(request,'login.html',context)















#صفحه دانش آموز
def studenttemplate(request, username):
    model = student
    text3 = student.objects.filter(user_name=username)[0]
    activation = text3.isactive
    f_name = text3.first_name
    l_name = text3.last_name
    student_id = text3.user_name
    student_grade = text3.Grade
    d = ' '    
    link = ' '
    s = ' '
    cfname = ' '
    if request.method == 'POST':
        form = changepassword(request.POST,request.FILES)
        if form.is_valid():
            t = form.cleaned_data['lpassword']
            t2 = form.cleaned_data['npassword']
            t3 = form.cleaned_data['npassword2']
            if text3.password == t and t2==t3 :
                setpassword = text3.password
                setpassword = t2
                text3.password = setpassword
                text3.save()
            else :
                d = 'اطلاعات وارد شده برای تغییر رمز عبور اشتباه است'


    else:
        form = changepassword()
        form2 = importfile()

    context = {
        'd' : d,
        'activation' : activation,
        'student_id' : student_id,
        'f_name': f_name,
        'l_name': l_name,
        'student_grade' : student_grade,
        'form' : form,
        'link' : link,
        's' : s,
    }

    return render(request, 'student.html', context)





#صفحه تکالیف جدید
def newhomeworks(request, username):
    model = student,deadline
    text3 = student.objects.filter(user_name=username)[0]
    activation = text3.isactive
    f_name = text3.first_name
    l_name = text3.last_name
    student_id = text3.user_name
    student_grade = text3.Grade
    d = ' '    
    link = ' '
    s = ' '
    cfname = ' '
    m = deadline.objects.all()[0]
    riaziday = m.rday
    riazihour = m.rhour
    fizikday = m.phday
    fizikhour = m.phhour
    shimiday = m.chday
    shimihour = m.chhour
    if request.method == 'POST':
        form = changepassword(request.POST,request.FILES)
        if form.is_valid():
            t = form.cleaned_data['lpassword']
            t2 = form.cleaned_data['npassword']
            t3 = form.cleaned_data['npassword2']
            if text3.password == t and t2==t3 :
                setpassword = text3.password
                setpassword = t2
                text3.password = setpassword
                text3.save()
            else :
                d = 'اطلاعات وارد شده برای تغییر رمز عبور اشتباه است'


    else:
        form = changepassword()
        form2 = importfile()

    context = {
        'd' : d,
        'activation' : activation,
        'student_id' : student_id,
        'f_name': f_name,
        'l_name': l_name,
        'student_grade' : student_grade,
        'form' : form,
        'link' : link,
        's' : s, 'riaziday' : riaziday, 'riazihour' : riazihour, 'fizikday' : fizikday, 'fizikhour' : fizikhour, 'shimiday' : shimiday, 'shimihour' : shimihour,
    }

    return render(request, 'newhomeworks.html', context)




#نمرات دانش آموز
def studentscorestemplate(request, username):
    model = student
    text3 = student.objects.filter(user_name=username)[0]
    activation = text3.isactive
    f_name = text3.first_name
    l_name = text3.last_name
    student_id = text3.user_name
    student_grade = text3.Grade
    cours = text3.taken_courses.all()
    r1=text3.rc
    r2=text3.rf
    r3=text3.rs
    
    ph1=text3.phc
    ph2=text3.phf
    ph3=text3.phs

    ch1=text3.chc
    ch2=text3.chf
    ch3=text3.chs
    fr = [r1,r2,r3]
    fph = [ph1, ph2, ph3]
    fch = [ch1, ch2,ch3]
    r=sum(fr)/3
    ph=sum(fph)/3
    ch=sum(fch)/3
    mm = [r,ph,ch]
    ff=sum(mm)/3
    ff = str(round(ff,2))


    d = ' '    
    link = ' '
    s = ' '
    cfname = ' '
    if request.method == 'POST':
        form = changepassword(request.POST,request.FILES)
        form2 = importfile(request.POST,request.FILES)
        uploaded_files = request.FILES['homework']
        if form2.is_valid():
            cname = form2.cleaned_data['coursename']
            cfname = cname + student_id +'.zip'
            uploaded_files.name = cfname
        fs = FileSystemStorage()
        lin = fs.save(uploaded_files.name,uploaded_files)
        link = fs.url(lin)
        s = 'فایلی که هم اکنون بارگذاری کردید'
        print(uploaded_files.name)

        if form.is_valid():
            t = form.cleaned_data['lpassword']
            t2 = form.cleaned_data['npassword']
            t3 = form.cleaned_data['npassword2']
            if text3.password == t and t2==t3 :
                setpassword = text3.password
                setpassword = t2
                text3.password = setpassword
                text3.save()
            else :
                d = 'اطلاعات وارد شده برای تغییر رمز عبور اشتباه است'


    else:
        form = changepassword()
        form2 = importfile()

    context = {
        'd' : d,
        'activation' : activation,
        'student_id' : student_id,
        'f_name': f_name,
        'l_name': l_name,
        'student_grade' : student_grade,
        'form' : form,
        'link' : link,
        's' : s,
        'form2' : form2,
        'r1' : r1, 'r2' : r2, 'r3' : r3, 'ph1' : ph1, 'ph2' : ph2, 'ph3' : ph3, 'ch1' : ch1, 'ch2' : ch2, 'ch3' : ch3, 
        'ff' : ff,
    }

    return render(request,'scores.html',context)






#صفحه ی دبیر
def teachertemplate(request,username):
    model = teacher, student
    text3 = teacher.objects.filter(user_name=username)[0]
    activation = text3.isactive
    f_name = text3.first_name
    l_name = text3.last_name
    student_id = text3.user_name
    student_grade = text3.field
    e = '0'
    if student_grade == 'ریاضی':
        e = 'r'
    elif student_grade == 'فیزیک':
        e = 'ph'
    elif student_grade == 'شیمی':
        e = 'ch'
    elif student_grade == 'ادبیات فارسی':
        e = 'p'
    elif student_grade == 'زبان انگلیسی':
        e = 'e'
    adress = []

    address = 'media/'+e+'981010101.zip','media/'+e+'981010102.zip','media/'+e+'971010101.zip','media/'+e+'971010102.zip','media/'+e+'961010101.zip','media/'+e+'961010102.zip'

    d = ' ' 
    riazi = 0
    fizik = 0
    shimi  = 0

    if student_grade == 'ریاضی':
        riazi = 1

    elif student_grade == 'فیزیک':
        fizik = 1
                  
    elif student_grade == 'شیمی':
        shimi  = 1
    
    if request.method == 'POST':
        form = changepassword(request.POST,request.FILES)
        if form.is_valid():
            t = form.cleaned_data['lpassword']
            t2 = form.cleaned_data['npassword']
            t3 = form.cleaned_data['npassword2']
            if text3.password == t and t2==t3 :
                setpassword = text3.password
                setpassword = t2
                text3.password = setpassword
                text3.save()
            else :
                d = 'اطلاعات وارد شده برای تغییر رمز عبور اشتباه است'


    else:
        form = changepassword()
  
    context = {
        'activation' : activation,
        'student_id' : student_id,
        'f_name': f_name,
        'l_name': l_name,
        'student_grade' : student_grade,
        'd' : d,
        'form' : form,
        'address' : address,
        'riazi' : riazi, 'fizik' : fizik, 'shimi' : shimi,
    }

    return render(request, 'teacher.html', context)



#صفحه ی تکالیف
def homework(request,username):
    model = teacher, student, deadline
    text3 = teacher.objects.filter(user_name=username)[0]
    activation = text3.isactive
    f_name = text3.first_name
    l_name = text3.last_name
    student_id = text3.user_name
    student_grade = text3.field
    e = '0'
    if student_grade == 'ریاضی':
        e = 'r'
    elif student_grade == 'فیزیک':
        e = 'ph'
    elif student_grade == 'شیمی':
        e = 'ch'
    adress = []
    
    address = 'media/'+e+'981010101.zip','media/'+e+'981010102.zip','media/'+e+'971010101.zip','media/'+e+'971010102.zip','media/'+e+'961010101.zip','media/'+e+'961010102.zip'

    d = ' ' 
    m = deadline.objects.all()[0]
    if request.method == 'POST':
        form = sethomework(request.POST,request.FILES)
        uploaded_files = request.FILES['addhomework']
        if form.is_valid():
            cfname = student_id +'.zip'
            uploaded_files.name = cfname
            Days = form.cleaned_data['days']
            Hours = form.cleaned_data['hours']
            m.rday = Days
            m.rhour = Hours
            m.save()
        
        fs = FileSystemStorage()
        lin = fs.save(uploaded_files.name,uploaded_files)
        link = fs.url(lin)
        s = 'فایلی که هم اکنون بارگذاری کردید'
        print(uploaded_files.name) 


    else:
        form = sethomework()
  
    context = {
        'activation' : activation,
        'student_id' : student_id,
        'f_name': f_name,
        'l_name': l_name,
        'student_grade' : student_grade,
        'd' : d,
        'form' : form,
        'address' : address,
    }

    return render(request, 'homework.html', context)








#صفحه اولیا
def parenttemplate(request,username):
    model = student
    text3 = student.objects.filter(my_parent = username)[0]
    f_name = text3.first_name
    l_name = text3.last_name
    student_id = text3.user_name
    student_grade = text3.Grade
    activation = text3.isactive

    r1=text3.rc
    r2=text3.rf
    r3=text3.rs
    
    ph1=text3.phc
    ph2=text3.phf
    ph3=text3.phs

    ch1=text3.chc
    ch2=text3.chf
    ch3=text3.chs

    fr = [r1,r2,r3]
    fph = [ph1, ph2, ph3]
    fch = [ch1, ch2,ch3]
    r=sum(fr)/3
    ph=sum(fph)/3
    ch=sum(fch)/3
    mm = [r,ph,ch]
    ff=sum(mm)/3
    ff = str(round(ff,2))

    
    context = {
        'activation' : activation,
        'student_id' : student_id,
        'f_name': f_name,
        'l_name': l_name,
        'student_grade' : student_grade,
        'r1' : r1, 'r2' : r2, 'r3' : r3, 'ph1' : ph1, 'ph2' : ph2, 'ph3' : ph3, 'ch1' : ch1, 'ch2' : ch2, 'ch3' : ch3, 
        'ff' : ff,
    }

    return render(request, 'parent.html', context)









#صفحه خروج
def loggingout(request, username):
    model = student,teacher
    if student.objects.filter(user_name=username) :
        text = student.objects.filter(user_name=username)[0]
        act = text.isactive
        act = False
        text.isactive = act
        text.save()
        
    elif teacher.objects.filter(user_name = username) :
        text2 = teacher.objects.filter(user_name = username)[0]
        act = text2.isactive
        act = False
        text2.isactive = act
        text2.save()


    return redirect('login')









#صفحه کلاس ها
def classtemplate(request, username):
    model = teacher
    text3 = teacher.objects.filter(user_name=username)[0]
    student_id = text3.user_name
    f_name = text3.first_name
    activation = text3.isactive
    l_name = text3.last_name
    student_grade = text3.field
    classes = text3.myclass.all()
    teacher_classes = []
    for x in range(3):
        teacher_classes.append(classes[x].class_name)
    
    d = ' ' 

    if request.method == 'POST':
        form = changepassword(request.POST,request.FILES)
        if form.is_valid():
            t = form.cleaned_data['lpassword']
            t2 = form.cleaned_data['npassword']
            t3 = form.cleaned_data['npassword2']
            if text3.password == t and t2==t3 :
                setpassword = text3.password
                setpassword = t2
                text3.password = setpassword
                text3.save()
            else :
                d = 'اطلاعات وارد شده برای تغییر رمز عبور اشتباه است'


    else:
        form = changepassword()

    
    e = '0'
    if student_grade == 'ریاضی':
        e = 'r'
    elif student_grade == 'فیزیک':
        e = 'ph'
    elif student_grade == 'شیمی':
        e = 'ch'
    elif student_grade == 'ادبیات فارسی':
        e = 'p'
    elif student_grade == 'زبان انگلیسی':
        e = 'e'
    adress = []

    address = 'media/'+e+'981010101.zip','media/'+e+'981010102.zip','media/'+e+'971010101.zip','media/'+e+'971010102.zip','media/'+e+'961010101.zip','media/'+e+'961010102.zip'

    
    contex = {
        'student_id' : student_id,
        'teacher_classes' : teacher_classes,
        'f_name' : f_name,
        'l_name' : l_name,
        'd' : d,
        'form' : form,
        'activation' : activation,
        'address' : address,
        'student_grade' : student_grade,

    }
    return render(request,'class.html', contex)












#داخل صفحه کلاس ها
def cinsidetemplate (request, username, number):
    model = teacher,student
    text3 = teacher.objects.filter(user_name=username)[0]
    student_id = text3.user_name
    f_name = text3.first_name
    l_name = text3.last_name
    student_grade = text3.field
    activation = text3.isactive
    num = number
    class_num = 'هیچی'
    if num == 1:
        class_num = 'اول'
    elif num == 2:
        class_num = 'دوم'
    elif num== 3:
        class_num = 'سوم'


    text2 = student.objects.filter(myclass = number)
    studentName = []
    studentID = []
    querysetlength = len(text2)
    for x in range(querysetlength):
        studentName.append(text2[x].first_name +' '+text2[x].last_name)
        studentID.append(text2[x].user_name)
        
    tcourse = text3.field
    sscourse = text2[0].taken_courses.all()
    scourse = '0'
    h = 0
    if request.method == 'POST':
        form = setscore(request.POST, request.FILES)
        if form.is_valid():
            s = form.cleaned_data['cscore']
            s2 = form.cleaned_data['fscore']
            s3 = form.cleaned_data['sscore']
            h = s4
            sscourse = text2[0].taken_courses.all()
            for sc in sscourse:
                if sc.course_name == tcourse:
                    sc.cscore = s
                    sc.fscore = s2
                    sc.sscore = s3
                    sc.save()
                    



    else :
        form = setscore()

    sscourse = text2[0].taken_courses.all()

    e = '0'
    if student_grade == 'ریاضی':
        e = 'r'
    elif student_grade == 'فیزیک':
        e = 'ph'
    elif student_grade == 'شیمی':
        e = 'ch'
    elif student_grade == 'ادبیات فارسی':
        e = 'p'
    elif student_grade == 'زبان انگلیسی':
        e = 'e'
    adress = []

    address = 'media/'+e+'981010101.zip','media/'+e+'981010102.zip','media/'+e+'971010101.zip','media/'+e+'971010102.zip','media/'+e+'961010101.zip','media/'+e+'961010102.zip'

    context = {
        'student_id' : student_id,
        'f_name' : f_name,
        'l_name' : l_name,
        'class_num' : class_num,
        'studentName' : studentName,
        'querysetlength' : querysetlength,
        'scourse' : scourse,
        'n' : h,
        'activation' : activation,
        'address' : address,
        'form' : form,
        'studentID': studentID,
        'student_grade' : student_grade,
    }

    return render(request, 'cinside.html', context)





#نمره گذاری
def putscore(request,username,number,who):

    model = teacher,student
    text3 = teacher.objects.filter(user_name=username)[0]
    student_id = text3.user_name
    f_name = text3.first_name
    l_name = text3.last_name
    student_grade = text3.field
    activation = text3.isactive
    num = number
    class_num = 'هیچی'
    if num == 1:
        class_num = 'اول'
    elif num == 2:
        class_num = 'دوم'
    elif num== 3:
        class_num = 'سوم'


    text2 = student.objects.filter(myclass = number)
    studentName = []
    querysetlength = len(text2)
    for x in range(querysetlength):
        studentName.append(text2[x].first_name +' '+text2[x].last_name)
        
    tcourse = text3.field
    sscourse = []
    scourse = '0'
    h = 0
    p = who - 1
    if request.method == 'POST':
        form = setscore(request.POST, request.FILES)
        if form.is_valid():
            s = form.cleaned_data['cscore']
            s2 = form.cleaned_data['fscore']
            s3 = form.cleaned_data['sscore']
            sscourse = text2[p].taken_courses.all()
            for sc in sscourse:
                if tcourse == 'ریاضی':
                    text2[p].rc = s
                    text2[p].rf = s2
                    text2[p].rs = s3
                    text2[p].save()
                elif tcourse == 'فیزیک':
                    text2[p].phc = s
                    text2[p].phf = s2
                    text2[p].phs = s3
                    text2[p].save()
                elif tcourse == 'شیمی':
                    text2[p].chc = s
                    text2[p].chf = s2
                    text2[p].chs = s3
                    text2[p].save()
    else :
        form = setscore()


    e = '0'
    if student_grade == 'ریاضی':
        e = 'r'
    elif student_grade == 'فیزیک':
        e = 'ph'
    elif student_grade == 'شیمی':
        e = 'ch'
    elif student_grade == 'ادبیات فارسی':
        e = 'p'
    elif student_grade == 'زبان انگلیسی':
        e = 'e'
    adress = []

    address = 'media/'+e+'981010101.zip','media/'+e+'981010102.zip','media/'+e+'971010101.zip','media/'+e+'971010102.zip','media/'+e+'961010101.zip','media/'+e+'961010102.zip'

    context = {
        'student_id' : student_id,
        'f_name' : f_name,
        'l_name' : l_name,
        'class_num' : class_num,
        'studentName' : studentName,
        'querysetlength' : querysetlength,
        'scourse' : scourse,
        'n' : h,
        'activation' : activation,
        'address' : address,
        'form' : form,
        'student_grade' : student_grade,
    }

    return render(request, 'putscore.html',context)




#نمره ها 
def getscore(request,username,number,who):

    model = teacher,student
    text3 = teacher.objects.filter(user_name=username)[0]
    student_id = text3.user_name
    f_name = text3.first_name
    l_name = text3.last_name
    student_grade = text3.field
    activation = text3.isactive
    num = number
    class_num = 'هیچی'
    if num == 1:
        class_num = 'اول'
    elif num == 2:
        class_num = 'دوم'
    elif num== 3:
        class_num = 'سوم'


    text2 = student.objects.filter(myclass = number)
    studentName = []
    querysetlength = len(text2)
    for x in range(querysetlength):
        studentName.append(text2[x].first_name +' '+text2[x].last_name)
        
    tcourse = text3.field
    sscourse = []
    scourse = '0'
    h = 0
    p = who - 1
    riazi = 0
    fizik = 0
    shimi = 0
    if tcourse == 'ریاضی':
        riazi = 1
        s = text2[p].rc 
        s2 = text2[p].rf 
        s3 = text2[p].rs
    elif tcourse == 'فیزیک':
        fizik = 1
        s = text2[p].phc 
        s2 = text2[p].phf
        s3 = text2[p].phs 
                  
    elif tcourse == 'شیمی':
        shimi  = 1
        s = text2[p].chc
        s2 = text2[p].chf 
        s3 = text2[p].chs
                 

    e = '0'
    if student_grade == 'ریاضی':
        e = 'r'
    elif student_grade == 'فیزیک':
        e = 'ph'
    elif student_grade == 'شیمی':
        e = 'ch'
    elif student_grade == 'ادبیات فارسی':
        e = 'p'
    elif student_grade == 'زبان انگلیسی':
        e = 'e'
    adress = []

    address = 'media/'+e+'981010101.zip','media/'+e+'981010102.zip','media/'+e+'971010101.zip','media/'+e+'971010102.zip','media/'+e+'961010101.zip','media/'+e+'961010102.zip'

    context = {
        'student_id' : student_id,
        'f_name' : f_name,
        'l_name' : l_name,
        'class_num' : class_num,
        'studentName' : studentName,
        'querysetlength' : querysetlength,
        'scourse' : scourse,
        'n' : h,
        'activation' : activation,
        'address' : address,
        's' : s, 's2' : s2, 's3' : s3,
        'student_grade' : student_grade,
        'riazi' : riazi, 'fizik' : fizik , 'shimi' : shimi,
    }

    return render(request, 'getscore.html',context)