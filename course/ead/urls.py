from django.urls import path
from course.ead import views

app_name = 'ead'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug>', views.detail, name='detail'),
]