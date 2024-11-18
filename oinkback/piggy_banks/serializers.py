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

	# 이런식으로 적을 수 있나?
	d_day = serializers.DateField(source='user_product.만기일자 - datetime.today', read_only=True)

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

