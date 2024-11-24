from rest_framework import serializers
from .models import PiggyBank
# from datetime import datetime
from django.utils.timezone import now
from django.contrib.auth import get_user_model

# 메인페이지 돼지저금통 조회
class PiggyListSerializer(serializers.ModelSerializer):
    
    class UserSerialzier(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'name',)

    user = UserSerialzier(read_only=True)

    class Meta:
        model = PiggyBank
        fields = '__all__'
        # fields = ('user', 'name', 'cheerup_count')
        read_only_fields = ('user',)


# 내 돼지저금통 조회
class PiggyDetailSerializer(serializers.ModelSerializer):
    # d_day 계산 로직
    d_day = serializers.SerializerMethodField()

    def get_d_day(self, obj):
        if obj.user_product.expiration_date:
            return (obj.user_product.expiration_date - now().date()).days
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
		read_only_fields = ('user', 'user_product')


