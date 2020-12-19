from django.urls import path

from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='test/login.html'), name='login'),
]
