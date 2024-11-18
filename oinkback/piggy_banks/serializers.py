from rest_framework import serializers
from .models import PiggyBank
from datetime import datetime

# 메인페이지 돼지저금통 조회
class PiggyListSerializer(serializers.ModelSerializer):
        
	class Meta:
		model = PiggyBank
		fields = ('user', 'name', 'cheerup_count')
		read_only_fields = ('user',)


# 내 돼지저금통 조회
class PiggyDetailSerializer(serializers.ModelSerializer):
    d_day = serializers.SerializerMethodField()

    def get_d_day(self, obj):
        # user_product 만기일자와 오늘 날짜를 비교
        if hasattr(obj, 'user_product') and obj.user_product:
            return (obj.user_product.만기일자 - date.today()).days
        return None

    class Meta:
        model = PiggyBank
        fields = '__all__'
        read_only_fields = ('user', 'user_product')


# 돼지저금통 생성, 수정
class PiggySerializer(serializers.ModelSerializer):

	class Meta:
		model = PiggyBank
		fields = '__all__'
		read_only_fiels = ('user', 'user_product')

