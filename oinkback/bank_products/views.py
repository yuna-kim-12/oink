from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import BankProductListSerializer, BankProductSerializer
from .models import BankProducts

# Create your views here.
# 예금상품 전체 리스트 조회 : 우대 금리 기준 내림차순
@api_view(['GET'])
def deposits(request):
    if request.method == 'GET':
        deposits = BankProducts.objects.filter(category=0).order_by('-prime_interest_rate')
        serializer = BankProductListSerializer(deposits, many=True)
        return Response(serializer.data)


# 적금상품 전체 리스트 조회 : 우대 금리 기준 내림차순
@api_view(['GET'])
def savings(request):
    if request.method == 'GET':
        savings = BankProducts.objects.filter(category=1).order_by('-prime_interest_rate')
        serializer = BankProductListSerializer(savings, many=True)
        return Response(serializer.data)

# 필터링한 예금상품 : 은행, 기간 기준 필터링 / 우대 금리 기준 내림차순
def filtered_deposits(request):
    if request.method == 'GET':
        deposits = BankProducts.objects.filter(category=0)
        vue_company_code = request.query_params.get('company_code', None)
        vue_join_period = request.query_params.get('join_period', None)
        # 문자열 contain으로 확인(vue에서 개월 수 문자열로 넘겨줘야 함)
        filtered_deposits = deposits.filter(company_code=vue_company_code, join_period__contains=vue_join_period).order_by('-prime_interest_rate')
        serializer = BankProductListSerializer(filtered_deposits, many=True)
        return Response(serializer.data)


def filtered_savings(request):
    if request.method == 'GET':
        savings = BankProducts.objects.filter(category=1)
        vue_company_code = request.query_params.get('company_code', None)
        vue_join_period = request.query_params.get('join_period', None)
        # 문자열 contain으로 확인(vue에서 개월 수 문자열로 넘겨줘야 함)
        filtered_savings = savings.filter(company_code=vue_company_code, join_period__contains=vue_join_period).order_by('-prime_interest_rate')
        serializer = BankProductListSerializer(filtered_savings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# 회원 정보 기반 추천 : 알고리즘 내일 확정
def products_recommend(request):
    if request.method == 'GET':
        savings = BankProducts.objects.filter(category=1)
        vue_company_code = request.query_params.get('company_code', None)
        vue_join_period = request.query_params.get('join_period', None)
        # 문자열 contain으로 확인(vue에서 개월 수 문자열로 넘겨줘야 함)
        filtered_savings = savings.filter(company_code=vue_company_code, join_period__contains=vue_join_period).order_by('-prime_interest_rate')
        serializer = BankProductListSerializer(filtered_savings, many=True)
        return Response(serializer.data)


def products_joined(request):
    pass