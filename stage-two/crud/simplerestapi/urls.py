from django.urls import path 
from . import views

urlpatterns = [
    path('api', views.PersonView.as_view()),
    path('api/<int:pk>', views.SinglePersonView.as_view()),
]