from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('/code=(?P<code>)', views.home),
    path('', views.home),
    path('student/', views.student),
    path('teacher/', views.teacher),
    path('studentLogin/', views.studentLogin),
    path('studentRegister/', views.studentRegister),
    path('teacherLogin/', views.teacherLogin),
    path('teacherRegister/', views.teacherRegister),
    path('getresponse/', views.getresponse),
    path('msg', views.messages),
    path('dashboard/', views.dashboard),
    path('summarize/', views.summarizer),
    path('feedback/', include('feedback.urls')),
    path('accounts/', include('accounts.urls'))
]

urlpatterns += staticfiles_urlpatterns()
