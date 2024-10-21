from django.contrib.auth.models import User
from django.db import models


# Create your models here.


# class User(models.Model):
#     id = models.IntegerField(primary_key=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    DOB = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.user} {self.DOB}'


class Semester(models.Model):
    year = models.IntegerField()
    semester = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.year} - {self.semester}'


class Course(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    staff_id = models.IntegerField()
    DOB = models.DateField()  # Date of Birth
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 1-to-1 relationship with User

    def __str__(self):
        return f'Lecturer {self.user}'


class Class(models.Model):
    class_id = models.IntegerField(primary_key=True)
    number = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Many classes can belong to one course
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)  # Many classes can happen in one semester
    lecturer = models.ForeignKey(Lecture, on_delete=models.CASCADE)  # Many classes can have one lecturer

    def __str__(self):
        return f'Class {self.number} for {self.course}'


class CollegeDay(models.Model):
    date = models.DateField()
    class_attended = models.ForeignKey(Class, on_delete=models.CASCADE)  # Many-to-one relationship with Class

    def __str__(self):
        return f'College Day on {self.date}'


class Attendance(models.Model):
    id = models.IntegerField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_attended = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField()

    def __str__(self):
        return f'{self.id} - {self.student} - {self.class_attended}'


from django.db import models

# Create your models here.
