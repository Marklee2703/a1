from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib import messages

from .forms import StudentForm, UserForm, SemesterForm, CourseForm
from .models import Semester, Course, Class, Lecture, Student, Attendance


# from .forms import SemesterForm, CourseForm, ClassForm, LecturerForm, StudentForm, AttendanceForm, UploadExcelForm
# from django.http import HttpResponse
# import openpyxl


# 1. login_page
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
    return render(request, 'login.html')


def home(request):
    user = request.user  # Get the currently logged-in user

    # Render the home page with the user context
    return render(request, 'home.html')


# 2. 管理员管理学期的视图
class SemesterListView(ListView):
    model = Semester
    template_name = 'semester_list.html'


class SemesterCreateView(CreateView):
    model = Semester
    form_class = SemesterForm
    template_name = 'semester_form.html'
    success_url = reverse_lazy('semester-list')


class SemesterDetailView(DetailView):
    model = Semester
    template_name = 'semester_detail.html'


#
class SemesterUpdateView(UpdateView):
    model = Semester
    form_class = SemesterForm
    template_name = 'semester_update.html'
    success_url = reverse_lazy('semester-list')


#
class SemesterDeleteView(DeleteView):
    model = Semester
    template_name = 'semester_delete.html'
    success_url = reverse_lazy('semester-list')


#
#
# # 3. 管理员管理课程的视图
class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'


#
#
class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course_create.html'
    success_url = reverse_lazy('course_list')
#
#
# class CourseUpdateView(UpdateView):
#     model = Course
#     form_class = CourseForm
#     template_name = 'admin/course_form.html'
#     success_url = reverse_lazy('course_list')
#
#
# class CourseDeleteView(DeleteView):
#     model = Course
#     template_name = 'admin/course_confirm_delete.html'
#     success_url = reverse_lazy('course_list')
#
#
# # 4. 管理员管理班级的视图
# class ClassListView(ListView):
#     model = Class
#     template_name = 'admin/class_list.html'
#
#
# class ClassCreateView(CreateView):
#     model = Class
#     form_class = ClassForm
#     template_name = 'admin/class_form.html'
#     success_url = reverse_lazy('class_list')
#
#
# class ClassUpdateView(UpdateView):
#     model = Class
#     form_class = ClassForm
#     template_name = 'admin/class_form.html'
#     success_url = reverse_lazy('class_list')
#
#
# class ClassDeleteView(DeleteView):
#     model = Class
#     template_name = 'admin/class_confirm_delete.html'
#     success_url = reverse_lazy('class_list')
#
#
# # 5. 管理员管理讲师的视图
# class LecturerListView(ListView):
#     model = Lecture
#     template_name = 'admin/lecturer_list.html'
#
#
# class LecturerCreateView(CreateView):
#     model = Lecture
#     form_class = LecturerForm
#     template_name = 'admin/lecturer_form.html'
#     success_url = reverse_lazy('lecturer_list')
#
#
# class LecturerUpdateView(UpdateView):
#     model = Lecture
#     form_class = LecturerForm
#     template_name = 'admin/lecturer_form.html'
#     success_url = reverse_lazy('lecturer_list')
#
#
# class LecturerDeleteView(DeleteView):
#     model = Lecture
#     template_name = 'admin/lecturer_confirm_delete.html'
#     success_url = reverse_lazy('lecturer_list')
#
#
# # 6. 管理员分配/移除讲师到班级的视图
# @login_required
# def assign_lecturer_to_class(request, class_id):
#     class_instance = get_object_or_404(Class, id=class_id)
#     if request.method == 'POST':
#         lecturer_id = request.POST.get('lecturer_id')
#         lecturer = get_object_or_404(Lecture, id=lecturer_id)
#         class_instance.lecturer = lecturer
#         class_instance.save()
#         messages.success(request, 'Lecturer assigned successfully!')
#         return redirect('class_list')
#     lecturers = Lecture.objects.all()
#     return render(request, 'admin/assign_lecturer.html', {'class_instance': class_instance, 'lecturers': lecturers})
#
#
# 7. 管理员管理学生的视图
class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_delete.html'
    success_url = reverse_lazy('student-list')


class StudentCreateView(CreateView):
    template_name = 'student_form.html'  # Replace with your template
    form_class = UserForm
    success_url = reverse_lazy('home')  # Redirect after successful creation

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        # Add the StudentForm to the context
        context['student_form'] = StudentForm()
        return context

    def form_valid(self, form):
        # Create User instance first
        user = form.save(commit=False)

        user.password = 'abc'  # Hash the password
        user.save()

        # Now create the Student instance
        student_form = StudentForm(self.request.POST)
        if student_form.is_valid():
            student = student_form.save(commit=False)
            student.user = user  # Link the Student to the User
            student.save()

        return super().form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_update.html'
    success_url = reverse_lazy('student-list')


#
#

#
#
# # 8. 管理员为学生报名/移除班级的视图
#
# @login_required
# def enrol_student_in_class(request, class_id):
#     class_instance = get_object_or_404(Class, id=class_id)
#     if request.method == 'POST':
#         student_id = request.POST.get('student_id')
#         student = get_object_or_404(Student, id=student_id)
#         class_instance.students.add(student)
#         messages.success(request, 'Student enrolled successfully!')
#         return redirect('class_list')
#     students = Student.objects.all()
#     return render(request, 'admin/enrol_student.html', {'class_instance': class_instance,
#                                                         'students': students})
#
#
# # 9. 管理员上传学生数据的视图
# @login_required
# def upload_students(request):
#     if request.method == 'POST':
#         form = UploadExcelForm(request.POST, request.FILES)
#         if form.is_valid():
#             excel_file = request.FILES['file']
#             wb = openpyxl.load_workbook(excel_file)
#             sheet = wb.active
#             for row in sheet.iter_rows(min_row=2, values_only=True):
#                 Student.objects.create(
#                     first_name=row[0],
#                     last_name=row[1],
#                     dob=row[2],
#                     email=row[3]
#                 )
#             messages.success(request, 'Students uploaded successfully!')
#             return redirect('student_list')
#     else:
#         form = UploadExcelForm()
#     return render(request, 'admin/upload_students.html', {'form': form})
#
#
# # 10. 讲师/管理员发送邮件视图
# @login_required
# def email_students_with_poor_attendance(request):
#     students = Student.objects.filter(attendance__lt=75)  # 假设低于75%为差出勤
#     if request.method == 'POST':
#         for student in students:
#             send_email_to_student(student)  # 假设有发送邮件的函数
#         messages.success(request, 'Emails sent successfully!')
#     return render(request, 'lecturer/email_students.html', {'students': students})
#
#
# # 11. 讲师登录视图
# def lecturer_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None and user.is_staff and hasattr(user, 'lecturer'):
#             login(request, user)
#             return redirect('lecturer_dashboard')
#         else:
#             messages.error(request, 'Invalid login credentials')
#     return render(request, 'lecturer/login.html')
#
#
# # 12. 讲师输入出勤数据的视图
# @login_required
# def record_attendance(request):
#     if request.method == 'POST':
#         form = AttendanceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Attendance recorded successfully!')
#             return redirect('attendance_list')
#     else:
#         form = AttendanceForm()
#     return render(request, 'lecturer/record_attendance.html', {'form': form})
#
#
# # 13. 学生登录视图
# def student_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None and hasattr(user, 'student'):
#             login(request, user)
#             return redirect('student_dashboard')
#         else:
#             messages.error(request, 'Invalid login credentials')
#     return render(request, 'student/login.html')
#
#
# # 14. 学生查看出勤情况的视图
def view_attendance(request):
    student = request.user.student
    attendance = Attendance.objects.filter(student=student)
    return render(request, 'student_attendance.html', {'attendance': attendance})
#
#
# from django.shortcuts import render
#
# # Create your views here.
