from django.urls import path
from polls import views

urlpatterns = [
    path('', views.index, name='polls_list'),
    path('<int:id>/details/', views.details, name='polls_details')
]