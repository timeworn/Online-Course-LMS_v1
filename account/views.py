from django.shortcuts import render, redirect
from django.contrib.auth import (
    views as auth_views,
    login as auth_login,
)
from LMS.constants import MEMBERSHIP, Student, Teacher, University
from .forms import StudentSignupForm, TeacherSignupForm, UniversitySignupForm
import json
# Create your views here.


class MyLoginView(auth_views.LoginView):

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        user = form.get_user()
        print(user.role)
        if user.is_superuser:
            return redirect('/admin/')
        if user.role == Student:
            return redirect('account:index')
        else:
            return redirect('account:pricing')


def index(request):
    return render(request, 'account/index.html')


def login(request):
    return render(request, 'account/login.html')


def pricing(request):
    print(MEMBERSHIP)
    return render(request, 'account/pricing.html', {'memberships': MEMBERSHIP})


def signup(request, membership_key=Student):
    membership = MEMBERSHIP[membership_key]
    form = None
    initial_data = None
    if 'membership_key' in request.session and 'signup_form_data' in request.session:
        initial_data = json.loads(request.session['signup_form_data'])
    if membership_key == Student:
        form = StudentSignupForm(initial=initial_data)
    elif membership_key == Teacher:
        form = TeacherSignupForm(initial = initial_data)
    elif membership_key == University:
        form = UniversitySignupForm(initial = initial_data)
    if request.method == 'POST':
        data = request.POST.dict()
        if membership_key == Student:
            form = StudentSignupForm(data=data)
        elif membership_key == Teacher:
            form = TeacherSignupForm(data=data)
        elif membership_key == University:
            form = UniversitySignupForm(data=data)

        if form.is_valid():
            request.session['signup_form_data'] = json.dumps(data)
            request.session['membership_key'] = membership_key
            return redirect('account:signup_payment', membership_key=membership_key, permanent =True)
    print(form.errors)
    return render(request, 'account/signup.html', {'membership': membership, 'form': form})


def signup_payment(request, membership_key=Student):
    print(request.session.keys())
    if 'membership_key' in request.session and 'signup_form_data' in request.session:
        if membership_key != request.session['membership_key']:
            return redirect('account:signup', membership_key=membership_key)
        if request.method == 'GET':
            membership = MEMBERSHIP[membership_key]
            return render(request, 'account/signup_payment.html', {'membership': membership})
        if request.method == 'POST':
            pass
            # form = None
            # session_data = request.session['signup_form_data']
            # data = json.loads(session_data)
            # if membership_key == Student:
            #     form = StudentSignupForm(data=data, initial={'username': data['initial']})
            # form.is_valid()
            # form.save()
    else:
        return redirect('account:signup', membership_key=membership_key)


def signup_success(request):
    membership_key = request.session.get('membership_key', Student)
    if 'membership_key' in request.session and 'signup_form_data' in request.session:
        session_data = request.session['signup_form_data']
        data = json.loads(session_data)
        if membership_key == Student:
            form = StudentSignupForm(data=data)
        elif membership_key == Teacher:
            form = TeacherSignupForm(data=data)
        elif membership_key == University:
            form = UniversitySignupForm(data=data)
        form.is_valid()
        form.save()
        del request.session['membership_key']
        del request.session['signup_form_data']
        return redirect('login')
    else:
        return redirect('account:signup', membership_key=membership_key)
