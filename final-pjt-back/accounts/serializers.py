from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
import re
from django.conf import settings
from piggy_banks.models import PiggyBank
from bank_products.models import UserProduct, BankProducts
from django.utils.timezone import now

User = get_user_model()


# 회원가입을 위한 커스텀 시리얼라이저
class CustomRegisterSerializer(RegisterSerializer):
    # username 필드 제거
    username = None
    # 기본 필드 외 추가 필드 정의
    # 커스텀 필드 추가
    name = serializers.CharField(required=True)
    birth_date = serializers.DateField(required=True)
    asset = serializers.IntegerField(required=True)
    saving_purpose = serializers.ListField(required=True)
    saving_amount = serializers.IntegerField(required=True)
    saving_period = serializers.IntegerField(required=True)

    def validate_password1(self, password):
        """비밀번호 유효성 검사"""
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
            raise serializers.ValidationError(
                "비밀번호는 8자 이상이며, 영문 대소문자, 숫자, 특수문자를 포함해야 합니다."
            )
        return password

    # 이메일 형식 유효성 검사
    def validate_email(self, email):
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise serializers.ValidationError("유효한 이메일 형식이 아닙니다.")
        return email

    # # 자산 금액 유효성 검사: 10,000원 단위
    # def validate_asset(self, amount):
    #     if amount % 10000 != 0:
    #         raise serializers.ValidationError("자산 금액은 10,000원 단위여야 합니다.")
    #     return amount
    
    # # 저축 금액 유효성 검사: 10,000원 단위
    # def validate_saving_amount(self, amount):
    #     """저축 금액 유효성 검사"""
    #     if amount % 10000 != 0:
    #         raise serializers.ValidationError("저축 금액은 10,000원 단위여야 합니다.")
    #     return amount

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data.update({
            'name': self.validated_data.get('name', ''),
            'birth_date': self.validated_data.get('birth_date', ''),
            'asset': self.validated_data.get('asset', ''),
            'saving_purpose': self.validated_data.get('saving_purpose', []),
            'saving_amount': self.validated_data.get('saving_amount', ''),
            'saving_period': self.validated_data.get('saving_period', '')
        })
        return data


    
# BankProductsSerializer 정의
class BankProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankProducts
        fields = ('product_name', 'company_name')  # 필요한 필드만 선택

# UserProductSerializer에서 BankProductsSerializer 중첩
class UserProductSerializer(serializers.ModelSerializer):
    product = BankProductsSerializer(read_only=True)  # BankProducts와 연결
    d_day = serializers.SerializerMethodField()


    def get_d_day(self, obj):
        # expiration_date가 None이 아닌 경우 d-day 계산
        if obj.expiration_date:
            return (obj.expiration_date.date() - now().date()).days
        return None  # 만료일이 없으면 None 반환

    # 납입 기간(개월)
    remain_month = serializers.SerializerMethodField()

    def get_remain_month(self, obj):
        # expiration_date가 None이 아닌 경우 d-day 계산
        if obj.join_date:
            return int((now().date() - obj.join_date.date()).days/30)+1
        return None  # 만료일이 없으면 None 반환

    class Meta:
        model = UserProduct
        fields = ('id', 'product', 'join_date', 'expiration_date', 'join_period', 'monthly_amount', 'interest_rate', 'd_day', 'remain_month',)

# PiggyBankSerializer에서 UserProductSerializer 중첩
class PiggyBankSerializer(serializers.ModelSerializer):
    user_product = UserProductSerializer(read_only=True)  # UserProduct와 연결

    class Meta:
        model = PiggyBank
        fields = ('id','name', 'weight', 'cheerup_count', 'saving_purpose', 'user_product')

# 사용자 정보 조회/수정을 위한 시리얼라이저
class CustomUserDetailsSerializer(serializers.ModelSerializer):    
    piggy_bank = PiggyBankSerializer(many=True, read_only=True)  # PiggyBank와 연결
    user_product = UserProductSerializer(many=True, read_only=True)
    
    # followers 필드를 사용자 이름 리스트로 변환
    followers = serializers.SerializerMethodField()
    followings = serializers.SerializerMethodField()


    # followers 필드에 대해 사용자 이름을 반환하는 메서드
    def get_followers(self, obj):
        return [{'name': follower.name, 'pk': follower.pk } for follower in obj.followers.all()]

    # followings 필드에 대해서도 동일하게 적용
    def get_followings(self, obj):
        return [{'name': following.name, 'pk':  following.pk} for following in obj.followings.all()]
    

    class Meta:
        model = get_user_model()
        fields = ('pk', 'email', 'name', 'birth_date', 'asset', 'saving_purpose', 
                  'saving_amount', 'saving_period', 'followers', 'followings', 'piggy_bank', 'user_product',)
        read_only_fields = ('pk', 'email', 'name', 'piggy_bank', 'user_product')