from django.db import models
from django.contrib.auth.models import AbstractUser
from LMS.constants import Student, Teacher, University
from django.conf import settings
from django_countries.fields import CountryField
# Create your models here.


class User(AbstractUser):
    USER_ROLE = [
        (Student, 'Student'),
        (Teacher, 'Teacher'),
        (University, 'University')
    ]
    role = models.CharField(max_length=10, choices=USER_ROLE, default=Student)
    avatar_url = models.ImageField(upload_to=settings.MEDIA_ROOT)
    about_me = models.TextField()
    subscribed = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=True)  # Admin verify the user


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    twitter_link = models.CharField(max_length=255)
    facebook_link = models.CharField(max_length=255)


class UniversityProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=255)
    country = CountryField(blank_label='(select country)')

# class StudentCourses(models.Model):
#     student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
#     course = models.ForeignKey('Course', on_delete=models.CASCADE)


# class PlatformFeedback(models.Model):
#     author = models.OneToOneField(User, on_delete=models.CASCADE)
#     rating_star = models.IntegerField()
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class FAQ(models.Model):
#     question = models.CharField(max_length=255)
#     answer = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class FAQVote(models.Model):
#     faq = models.ForeignKey('FAQ', on_delete=models.CASCADE)
#     user = models.ForeignKey('User', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class Category(models.Model):  # Topic
#     name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class Course(models.Model):
#     category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     trailer_video_link = models.CharField(max_length=255)
#     price = models.IntegerField()
#     thumbnail_url = models.ImageField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class Section(models.Model):  # course consists of several Section
#     course = models.ForeignKey('Course', on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)


# class Lesson(models.Model):  # lesson subsection of Section
#     section = models.ForeignKey('Section', on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     description = models.TextField(max_length=255)
#     video_url = models.CharField(max_length=255)
