from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import User, StudentProfile, TeacherProfile, UniversityProfile
from LMS.constants import Student, University, Teacher


class StudentSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Your email address ...'
        self.fields['password'].widget.attrs['placeholder'] = 'Your password ...'

    def clean(self):
        email = self.cleaned_data.get('email')
        username = email
        if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
            raise forms.ValidationError({'email': ["Email is already exists"]})
        return self.cleaned_data

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = Student
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password'])
        user.subscribed = True
        if commit:
            user.save()
        student_profile = StudentProfile.objects.create(user=user)
        student_profile.save()
        return user


class TeacherSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Your email address ...'
        self.fields['password'].widget.attrs['placeholder'] = 'Your password ...'

    def clean(self):
        email = self.cleaned_data.get('email')
        username = email
        if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
            raise forms.ValidationError({'email': ["Email is already exists"]})
        return self.cleaned_data

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = Teacher
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password'])
        user.subscribed = True
        if commit:
            user.save()
        profile = TeacherProfile.objects.create(user=user)
        profile.save()
        return user


class UniversitySignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    organization = forms.CharField()
    country = CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget())

    class Meta:
        model = User
        fields = ("email", "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Your email address ...'
        self.fields['password'].widget.attrs['placeholder'] = 'Your password ...'
        self.fields['organization'].widget.attrs['placeholder'] = 'Organization'

    def clean(self):
        email = self.cleaned_data.get('email')
        username = email
        organization = self.cleaned_data.get('organization')
        if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
            raise forms.ValidationError({'email': ["Email is already exists"]})
        if UniversityProfile.objects.filter(organization_name = organization).exists():
            raise forms.ValidationError({'organization': ["Organization Name is already exists"]})
        return self.cleaned_data

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = University
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password'])
        user.subscribed = True
        user.is_verified = False
        if commit:
            user.save()
        profile = UniversityProfile.objects.create(user=user)
        profile.organization_name = self.cleaned_data['organization']
        profile.country = self.cleaned_data['country']
        profile.save()
        return user
