from django import forms

from attendance.models import Student, User, Semester, Course


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password', 'username', 'first_name', 'last_name', 'email']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('student_id', 'DOB')

        widgets = {
            'student_id': forms.TextInput(
                attrs={'id': 'student_id', 'class': 'form-control', 'placeholder': 'student_id'}),
            'DOB': forms.TextInput(attrs={'id': 'DOB', 'class': 'form-control', 'placeholder': 'Date of Birth'}), }


class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = '__all__'


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
