from django.shortcuts import render
from account.decorators import role_required
from LMS.constants import Student
# Create your views here.


@role_required(role=Student)
def my_courses(request):

    return render(request, 'student/student_courses.html')
