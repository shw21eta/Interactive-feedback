from django.urls import path
from . import views

urlpatterns = [
    path('', views.messages),
    path('getFeedback/', views.getFeedback)
]
