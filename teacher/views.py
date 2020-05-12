from django.shortcuts import render, redirect, get_object_or_404
from course.forms import CourseEditForm, SectionEditForm, LessonEditForm
from course.models import Course, Section, Lesson
from account.decorators import role_required
from LMS.constants import Student, University, Teacher
from django.views.decorators.http import require_http_methods

# Create your views here.


def dashboard(request):
    return render(request, 'teacher/dashboard.html')


@role_required(role=Teacher)
def manage_courses(request):
    if request.method == 'GET':
        courses = Course.objects.filter(author=request.user).all()
        return render(request, 'teacher/manage_courses.html', {'courses': courses})


@role_required(role=Teacher)
def add_course(request):
    if request.method == 'GET':
        form = CourseEditForm(initial={'author': request.user})
    if request.method == 'POST':
        form = CourseEditForm(data=request.POST, files=request.FILES,)
        if form.is_valid():
            course = form.save()
            return redirect('teacher:edit_course', pk=course.pk)
    return render(request, 'teacher/add_course.html', {'form': form})


@role_required(role=Teacher)
def edit_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = CourseEditForm(instance=course)
    section_form = SectionEditForm()
    lesson_form = LessonEditForm()
    if request.method == 'POST':
        form = CourseEditForm(data=request.POST, files=request.FILES, instance=course)
        if form.is_valid():
            course = form.save()
            return redirect('teacher:edit_course', pk=course.pk)
    return render(request, 'teacher/edit_course.html', {'course': course, 'form': form, 'section_form': section_form, 'lesson_form': lesson_form})


@require_http_methods(["POST"])
@role_required(role=Teacher)
def add_section(request, pk):
    if request.method == 'POST':
        course = get_object_or_404(Course, pk=pk)
        form = SectionEditForm(data=request.POST)
        if form.is_valid():
            section = form.save(commit=False)
            section.course = course
            section.save()
    return redirect('teacher:edit_course', pk=course.pk)


@require_http_methods(["POST"])
@role_required(role=Teacher)
def add_lesson(request, section_pk):
    if request.method == 'POST':
        section = get_object_or_404(Section, pk=section_pk)
        form = LessonEditForm(data=request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.section = section
            lesson.save()
        return redirect('teacher:edit_course', pk=section.course.pk)


@require_http_methods(["POST"])
@role_required(role=Teacher)
def edit_delete_section(request, pk):
    section = get_object_or_404(Section, pk=pk)
    course_pk = section.course.pk
    if request.method == 'POST':
        action = request.POST.get('action', 'POST')
        if action == 'delete':
            section.delete()
        else:
            form = SectionEditForm(data=request.POST, instance=section)
            if form.is_valid():
                form.save()
    return redirect('teacher:edit_course', pk=course_pk)


@require_http_methods(["POST"])
@role_required(role=Teacher)
def edit_delete_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    course_pk = lesson.section.course.pk
    if request.method == 'POST':
        action = request.POST.get('action', 'POST')
        if action == 'delete':
            lesson.delete()
        else:
            form = LessonEditForm(data=request.POST, instance=lesson)
            if form.is_valid():
                form.save()
    return redirect('teacher:edit_course', pk=course_pk)


def earnings(request):
    return render(request, 'teacher/earning.html')


def statement(request):
    return render(request, 'teacher/statement.html')


def profile(request):
    return render(request, 'teacher/profile.html')
