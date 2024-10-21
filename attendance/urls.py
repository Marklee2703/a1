"""
URL configuration for a1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from attendance import views
from django.contrib.auth import views as auth_views

from attendance.views import view_attendance

urlpatterns = [

    # path('login/', views.login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),

    path('attendance/student', view_attendance, name='student-attendance'),

    path('student/create', views.StudentCreateView.as_view(), name='student-create'),
    path('student/', views.StudentListView.as_view(), name='student-list'),
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
    path('student/<int:pk>/delete', views.StudentDeleteView.as_view(), name='student-delete'),
    path('student/<int:pk>/update', views.StudentUpdateView.as_view(), name='student-update'),

    path('semester', views.SemesterListView.as_view(), name='semester-list'),
    path('semester/create', views.SemesterCreateView.as_view(), name='semester-create'),

    path('semester/<int:pk>', views.SemesterDetailView.as_view(), name='semester-detail'),

    path('semester/<int:pk>/update',views.SemesterUpdateView.as_view(), name='semester-update'),

    path('semester/<int:pk>/delete', views.SemesterDeleteView.as_view(), name='semester-delete'),


    path('course/create', views.CourseListView.as_view(), name='course-create'),



]
