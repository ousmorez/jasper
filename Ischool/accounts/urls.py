from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

pp_name = 'accounts'
urlpatterns=[
    path('', views.login, name ='login'),
    path('student/<int:username>/', views.studenttemplate, name='student'),
    path('student/<int:username>/scores/', views.studentscorestemplate, name='scores'),
    path('student/<int:username>/scores/newhomeworks/', views.newhomeworks, name='newhomeworks'),
    path('teacher/<int:username>/', views.teachertemplate, name='teacher'),
    path('teacher/<int:username>/homework/', views.homework, name='homework'),
    path('teacher/<int:username>/class/', views.classtemplate, name='class'),
    path('teacher/<int:username>/class/cinside/<int:number>/', views.cinsidetemplate, name='cinside'),
    path('teacher/<int:username>/class/cinside/<int:number>/<int:who>', views.putscore, name='putscore'),
    path('teacher/<int:username>/class/cinside/<int:number>/get/<int:who>', views.getscore, name='getscore'),
    path('parent/<int:username>/', views.parenttemplate, name='parent'),
    path('logout/<int:username>', views.loggingout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)