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

from attendance.views import view_attendance, lecture_login

urlpatterns = [

    # path('login/', views.login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),

    path('attendance/student', view_attendance, name='student-attendance'),
    path('attendance/lecture/class', lecture_login, name='lecture-login'),

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


    path('course/create', views.CourseCreateView.as_view(), name='course-create'),

    path('course/list', views.CourseListView.as_view(), name='course-list'),

    path('course/<int:pk>', views.CourseDetailView.as_view(), name='course-detail'),

    path('course/<int:pk>/update', views.CourseUpdateView.as_view(), name='course-update'),

    path('course/<int:pk>/delete', views.CourseDeleteView.as_view(), name='course-delete'),


    path('class/create', views.ClassCreateView.as_view(), name='class-create'),

    path('class/list', views.ClassListView.as_view(), name='class-list'),

    path('class/<int:pk>', views.ClassDetailView.as_view(), name='class-detail'),

    path('class/<int:pk>/update', views.ClassUpdateView.as_view(), name='class-update'),

    path('class/<int:pk>/delete', views.ClassDeleteView.as_view(), name='class-delete'),

    path('lecture/create', views.LectureCreateView.as_view(), name='lecture-create'),

    path('lecture/list', views.LectureListView.as_view(), name='lecture-list'),

    path('lecture/<int:pk>', views.LectureDetailView.as_view(), name='lecture-detail'),

    path('lecture/<int:pk>/update', views.LectureUpdateView.as_view(), name='lecture-update'),

    path('lecture/<int:pk>/delete', views.LectureDeleteView.as_view(), name='lecture-delete'),






]
