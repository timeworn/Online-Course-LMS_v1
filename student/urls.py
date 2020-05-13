from django.urls import path, include
from . import views
app_name = 'student'
urlpatterns = [
    path('my_courses', views.my_courses, name='my_courses')
]
