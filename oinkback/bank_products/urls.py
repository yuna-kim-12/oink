from django.urls import path
from . import views

urlpatterns = [
    path('deposits/', views.deposits),
    path('savings/', views.savings),
    path('deposit_detail/<int:product_pk>/', views.deposit_detail),
    path('savings_detail/<int:product_pk>/', views.savings_detail),
    path('filtered_deposits/', views.filtered_deposits),
    path('filtered_savings/', views.filtered_savings),
    path('products_recommend_deposits/', views.products_recommend_deposits),
    path('products_recommend_savings/', views.products_recommend_savings),
    path('products_joined/<int:user_pk>/', views.products_joined),
]
