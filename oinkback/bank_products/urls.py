from django.urls import path
from . import views

urlpatterns = [
    path('deposits/', views.deposits),
    path('savings/', views.savings),
    path('filtered_deposits/', views.filtered_deposits),
    path('filtered_savings/', views.filtered_savings),
    path('products_recommend_deposits/', views.products_recommend),
    path('products_recommend_savings/', views.products_recommend),
    path('products_joined/', views.products_joined),
]
