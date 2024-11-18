from rest_framework import serializers
from .models import PiggyBank

#### 아직 수정 많이 필요

# 내 돼지저금통 조회
class PiggyDetailSerializer(serializers.ModelSerializer):


    class Meta:
        model = PiggyBank
        fields = '__all__'
        read_only_fields = ('user', 'user_product')
