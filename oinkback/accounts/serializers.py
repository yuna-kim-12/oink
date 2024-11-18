from rest_framework import serializers
from django.conf import settings
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
import re

# 회원가입을 위한 커스텀 시리얼라이저
class CustomRegisterSerializer(RegisterSerializer):
    # 기본 필드 외 추가 필드 정의
    email = serializers.EmailField(required=True)
    name = serializers.CharField(required=True)
    birth_date = serializers.DateField(required=True)
    saving_purpose = serializers.ListField(required=True)
    saving_amount = serializers.IntegerField(required=True)
    saving_period = serializers.IntegerField(required=True)

    # 비밀번호 유효성 검사: 영문 대소문자, 숫자, 특수문자 포함 8자 이상
    def validate_password1(self, password):
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

    # 저축 금액 유효성 검사: 10,000원 단위
    def validate_saving_amount(self, amount):
        if amount % 10000 != 0:
            raise serializers.ValidationError("저축 금액은 10,000원 단위여야 합니다.")
        return amount

    # 유효성 검사를 통과한 데이터 반환
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data.update({
            'name': self.validated_data.get('name', ''),
            'birth_date': self.validated_data.get('birth_date', ''),
            'saving_purpose': self.validated_data.get('saving_purpose', []),
            'saving_amount': self.validated_data.get('saving_amount', ''),
            'saving_period': self.validated_data.get('saving_period', '')
        })
        return data

# 사용자 정보 조회/수정을 위한 시리얼라이저
class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('pk', 'email', 'name', 'birth_date', 'saving_purpose', 
                 'saving_amount', 'saving_period')
        read_only_fields = ('email', 'name', )  #  수정 불가