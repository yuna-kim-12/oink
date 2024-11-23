from django.shortcuts import render
from django.conf import settings
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse 
from .serializers import ExchangeSerializer
from .models import Exchange
import schedule
import time
from datetime import date



def update_exchange():
    # 오늘 날짜의 데이터가 이미 존재하는지 확인
    if Exchange.objects.filter(date=date.today()).exists():
        print("Today's exchange rates already exist.")
        return None  # 이미 데이터가 있으면 API 호출하지 않음

    # 금융 상품 저장하기.
    API_KEY = settings.EXCHANGE_API_KEY
    URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
    params = {
        'authkey': API_KEY,
        'data': 'AP01'
    }

    try:
        # SSL 검증 비활성화
        response = requests.get(URL, params=params, verify=False)
        products = response.json()
		print(products)

        # for product in products:
        #     cur_unit = product.get('cur_unit')
        #     cur_nm = product.get('cur_nm')
        #     deal_bas_r = product.get('deal_bas_r')

        #     # 오늘 날짜의 동일한 통화 정보가 없을 때만 저장
        #     if not Exchange.objects.filter(cur_unit=cur_unit, date=date.today()).exists():
        #         save_data = {
        #             'cur_unit': cur_unit,
        #             'cur_nm': cur_nm,
        #             'deal_bas_r': float(deal_bas_r.replace(',', '')),
        #             'date': date.today()
        #         }

        #         serializer = ExchangeSerializer(data=save_data)
        #         if serializer.is_valid(raise_exception=True):
        #             serializer.save()

        # print("Exchange rates updated successfully.")
        # return Response(status=status.HTTP_200_OK)

    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

update_exchange()