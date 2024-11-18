from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404

from .models import PiggyBank
from .serializers import PiggyDetailSerializer


# Create your views here.


@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def piggy_list(request):
    # 돼지저금통 조회
    if request.method == 'GET':
        piggy = PiggyBank.objects.all()
        serializer = ???Serializer(piggy)
        return Response(serializer.data)

    # 돼지저금통 생성
    elif request.method == 'POST':
        serializer = ???Serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)




@permission_classes([IsAuthenticated])
@api_view(['PUT', 'DELETE'])
def update_piggy(request, piggy_bank_pk):
    piggy = get_object_or_404(PiggyBank, pk=piggy_bank_pk)

    if piggy.user == request.user:
        # 돼지저금통 수정
        if request.method == 'PUT':
            serializer = ???Serializer(piggy, data=request.data)
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
    # 돼지저금통 응원
    cheerup_piggy = get_object_or_404(PiggyBank, pk=cheerup_piggy_bank_pk)
    cheerup_piggy.cheerup_count += 1
    cheerup_piggy.save()
    serializer = ???Serializer(cheerup_piggy)
    return Response(serializer.data)
