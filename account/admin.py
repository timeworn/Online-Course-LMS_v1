from django.contrib import admin
from .models import User, UniversityProfile


class UserAdmin(admin.ModelAdmin):
    model = User


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(UniversityProfile)
