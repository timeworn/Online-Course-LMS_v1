from django.urls import path, include
from . import views
app_name = 'teacher'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('manage_courses/', views.manage_courses, name='manage_courses'),
    path('add_course/', views.add_course, name='add_course'),
    path('edit_course/<int:pk>/', views.edit_course, name='edit_course'),
    path('add_section/<int:pk>', views.add_section, name='add_section'),
    path('add_lesson/<int:section_pk>', views.add_lesson, name='add_lesson'),
    path('edit_delete_section/<int:pk>', views.edit_delete_section, name='edit_delete_section'),
    path('edit_delete_lesson/<int:pk>', views.edit_delete_lesson, name='edit_delete_lesson'),
    path('earnings/', views.earnings, name='earnings'),
    path('statement/', views.statement, name='statement'),
    path('profile/', views.profile, name='profile'),
]
