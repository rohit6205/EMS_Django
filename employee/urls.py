from django.urls import path
from employee import views

urlpatterns = [
    path('', views.hello, name='employee_name'),
]