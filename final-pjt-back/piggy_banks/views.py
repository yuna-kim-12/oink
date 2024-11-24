from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import F

from .models import PiggyBank
from .serializers import PiggyListSerializer, PiggySerializer, PiggyDetailSerializer

from bank_products.models import UserProduct

import json



# Create your views here.
# @permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def piggy_list(request):
    # 메인페이지 돼지저금통 조회
    if request.method == 'GET':
        # 데이터 보고 50개 끊기 수정
        piggys = PiggyBank.objects.all().order_by('-created_at')[:20]
        serializer = PiggyListSerializer(piggys, many=True)
        return Response(serializer.data)

    # 돼지저금통 생성
    elif request.method == 'POST' & request.user:
        if PiggyBank.objects.filter(user=request.user).exists():
            return Response({'detail': '이미 돼지저금통이 있습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        
        print('=== Request Debug Info ===')
        print('Method:', request.method)
        print('Path:', request.path)
        print('Data:', request.data)
        print('User:', request.user)
        print('Headers:', request.headers)
        print('========================')

        # request.data에서 user_product_pk를 가져옴
        try:
            user_product_pk = request.data.get('user_product')
            print('user_product_pk:', user_product_pk)  # 디버깅용
            
            user_product = UserProduct.objects.get(pk=user_product_pk)
            print('user_product found:', user_product)  # 디버깅용
            
            serializer = PiggySerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user, user_product=user_product)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                
        except Exception as e:
            print('Error:', str(e))  # 디버깅용
            return Response({'detail': str(e)}, 
                          status=status.HTTP_400_BAD_REQUEST)


        # # JSON 데이터 파싱
        # try:
        #     data = json.loads(request.body)  # JSON 데이터를 파싱
        #     user_product_pk = request.query_params.get('user_product', None)
        #     user_product = UserProduct.objects.get(pk=user_product_pk)

        #     serializer = PiggySerializer(data=data)
        #     if serializer.is_valid(raise_exception=True):
        #         serializer.save(user=request.user, user_product=user_product)
        #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        # except json.JSONDecodeError:
        #     return Response({'detail': '잘못된 JSON 데이터입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        # except UserProduct.DoesNotExist:
        #     return Response({'detail': '유효하지 않은 UserProduct입니다.'}, status=status.HTTP_400_BAD_REQUEST)


        # user_product_pk = request.query_params.get('user_product', None)
        # user_product = UserProduct.objects.get(pk=user_product_pk)
        # # user_product는 vue에서 사용자가 선택하는데 그것이 request.data로 잘 들어갈지?
        # serializer = PiggySerializer(data=request.data)

        # if serializer.is_valid(raise_exception=True):
        #     serializer.save(user=request.user, user_product=user_product)
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)




@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE'])
def piggy_detail(request, piggy_bank_pk):
    piggy = get_object_or_404(PiggyBank, pk=piggy_bank_pk)

    # 내 돼지저금통 조회
    if request.method == 'GET':
        serializer = PiggyDetailSerializer(piggy)
        return Response(serializer.data)

    if piggy.user == request.user:
        # 돼지저금통 수정
        if request.method == 'PUT':
            serializer = PiggySerializer(piggy, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)

        # 돼지저금통 삭제
        elif request.method == 'DELETE':
            piggy.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    # 돼지저금통을 만든 유저가 아닐 경우
    else:
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)



@permission_classes([IsAuthenticated])
@api_view(['POST'])
def cheerup(request, cheerup_piggy_bank_pk):
    piggy = get_object_or_404(PiggyBank, pk=cheerup_piggy_bank_pk)
    piggy.cheerup_count = F('cheerup_count') + 1
    piggy.save(update_fields=['cheerup_count'])
    piggy.refresh_from_db()  # F() 업데이트 후 최신 값 불러오기
    serializer = PiggySerializer(piggy)
    return Response(serializer.data)
