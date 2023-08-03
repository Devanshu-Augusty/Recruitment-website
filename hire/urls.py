from django.urls import path
from hire import views

# id pass: devanshu 123456

urlpatterns = [
    path('', views.index, name='home'),
    path('job_post/', views.job_post, name='job_post'),
    path('jobs/', views.jobs, name='jobs'),
]