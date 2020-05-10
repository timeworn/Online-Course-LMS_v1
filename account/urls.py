from django.urls import path, include
from . import views
app_name = 'account'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('verify_email/', views.verify_email, name='verify_email'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('signup/success/', views.signup_success, name='signup_success'),
    path('signup/<slug:membership_key>/', views.signup, name='signup'),
    path('signup/<slug:membership_key>/payment/', views.signup_payment, name='signup_payment'),
    path('pricing/', views.pricing, name='pricing'),
]
