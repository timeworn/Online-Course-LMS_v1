from django.urls import path, include
from . import views
app_name = 'course'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('course/detail/<int:pk>/', views.course_detail, name='course_detail'),
    path('course/pay/<int:pk>/', views.course_pay, name='pay'),
    path('lesson/<int:pk>', views.lesson, name='lesson'),
    path('course/<int:pk>/trailor', views.watch_trailor, name='watch_trailor'),
    path('filter/', views.filter, name='filter')
]
