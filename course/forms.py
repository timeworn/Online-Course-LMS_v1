from django import forms
# from django.conf import settings
# from django.contrib.auth.forms import UserCreationForm
# from django.db import transaction
# from django_countries.fields import CountryField
# from django_countries.widgets import CountrySelectWidget
# from account.models import User, StudentProfile, TeacherProfile, UniversityProfile
from .models import Course, Section, Lesson, User
# from LMS.constants import Student, University, Teacher
# End


class CourseEditForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Course
        fields = '__all__'


class SectionEditForm(forms.ModelForm):

    class Meta:
        model = Section
        exclude = ('course', )


class LessonEditForm(forms.ModelForm):

    class Meta:
        model = Lesson
        exclude = ('section', 'duration', )


# class StudentSignupForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())

#     class Meta:
#         model = User
#         fields = ("first_name", "last_name", "email", "password")

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
#         self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
#         self.fields['email'].widget.attrs['placeholder'] = 'Your email address ...'
#         self.fields['password'].widget.attrs['placeholder'] = 'Your password ...'

#     def clean(self):
#         email = self.cleaned_data.get('email')
#         username = email
#         if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
#             raise forms.ValidationError({'email': ["Email is already exists"]})
#         return self.cleaned_data

#     @transaction.atomic
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.role = Student
#         user.email = self.cleaned_data['email']
#         user.username = self.cleaned_data['email']
#         user.set_password(self.cleaned_data['password'])
#         user.subscribed = True
#         if commit:
#             user.save()
#         student_profile = StudentProfile.objects.create(user=user)
#         student_profile.save()
#         send_email_verification_code(user, user.email)
#         return user
