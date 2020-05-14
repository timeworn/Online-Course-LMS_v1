from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from account.decorators import role_required
from LMS.constants import Student
from .models import Course, Lesson, Category
# Create your views here.


def filter(request):
    if request.method == 'GET':
        per_page = 3
        category = request.GET.get('category', None)
        search = request.GET.get('search', None)
        sort_by = request.GET.get('sort_by', None)
        queryset = Course.objects
        if category:
            queryset = queryset.filter(category__id=category)
        if search:
            queryset = queryset.filter(Q(title__contains=search) | Q(description__contains=search))
        if sort_by == 'OF':
            queryset = queryset.order_by('updated_at')
        elif sort_by == 'TAZ':
            queryset = queryset.order_by('title')
        elif sort_by == 'TZA':
            queryset = queryset.order_by('-title')
        else:
            queryset = queryset.order_by('-updated_at')

        course_list = queryset.all()

        paginator = Paginator(course_list, per_page)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        categorys = Category.objects.all()

        params = request.GET.dict()
        if category:
            params['category'] = int(params['category'])
            params['category_name'] = Category.objects.get(pk=category).name
        if not sort_by:
            params['sort_by'] = 'NF'
        return render(request, 'course/filters.html', {'page_obj': page_obj, 'categorys': categorys, 'params': params})


def index(request):
    courses = Course.objects.all()
    return render(request, 'course/index.html', {'top_courses': courses})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.user.is_authenticated:
        is_purchased_course = request.user.is_purchased(course)
    else:
        is_purchased_course = False
    return render(request, 'course/course_detail.html', {'course': course, 'is_purchased_course': is_purchased_course})


@role_required(role=Student)
def course_pay(request, pk):
    course = get_object_or_404(Course, pk=pk)
    request.user.studentprofile.courses.add(course)
    return redirect('course:course_detail', pk=pk)


@role_required(role=Student)
def lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    course = lesson.section.course
    if not request.user.is_purchased(course):
        return redirect('course:course_detail', pk=course.pk)
    return render(request, 'course/lesson.html', {'lesson': lesson, 'course': course})


def watch_trailor(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'course/watch_trailor.html', {'course': course})
