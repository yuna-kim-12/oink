from django.urls import path
from . import views

urlpatterns = [
    path('follow/<int:following_user_pk>/', views.follow),
]