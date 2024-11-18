from django.urls import path
from . import views


urlpatterns = [
    # 돼지저금통 조회, 생성
    path('', views.piggy_list),
    # 돼지저금통 수정, 삭제
    path('update_piggy/<int:piggy_bank_pk>/', views.update_piggy),
    # 돼지저금통 응원
    path('cheerup/<int:cheerup_piggy_bank_pk>/', views.cheerup),
]
