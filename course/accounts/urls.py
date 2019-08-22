from django.urls import path
from django.contrib.auth import views
from course.accounts import views as account_views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('cadastre-se/', account_views.register, name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
