from django.db import models
from django.contrib.auth.models import AbstractUser
from LMS.constants import Student, Teacher, University
from django.conf import settings
from django_countries.fields import CountryField
from account.models import User, StudentProfile, TeacherProfile, UniversityProfile
# Create your models here.


class Course(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    description = models.TextField()
    trailer_video_link = models.CharField(max_length=255)
    price = models.IntegerField()
    thumbnail_url = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_lesson_number(self):
        total_cnt = 0
        for section in self.section_set.all():
            total_cnt = total_cnt + section.lesson_set.count()
        return total_cnt


class Category(models.Model):  # Topic
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Section(models.Model):  # course consists of several Section
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Lesson(models.Model):  # lesson subsection of Section
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    duration = models.IntegerField(default=0)
    video_url = models.CharField(max_length=255)

    def __str__(self):
        return self.title


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
