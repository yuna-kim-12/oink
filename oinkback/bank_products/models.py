from django.db import models
from django.conf import settings

# Create your models here.
class BankProducts(models.Model):
    category = models.IntegerField()
    company_code = models.TextField()
    company_name = models.TextField()
    product_code = models.TextField()
    product_name = models.TextField()
    interest_rate = models.FloatField()
    prime_interest_rate = models.FloatField()
    product_link = models.TextField()
    join_period = models.TextField()
    join_period_text = models.TextField()
    join_amount_min = models.IntegerField()
    # null값 : 최대 금액 제한 없음
    join_amount_max = models.IntegerField(null=True, blank=True)
    join_amount_text = models.TextField()
    join_way = models.TextField(null=True, blank=True)
    join_member = models.TextField()
    prime_conditions = models.TextField(null=True, blank=True)
    interest_payment = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)



class UserProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 사용자 1명이 가입한 예적금 상품 / 역참조 : 예적금 상품에 가입한 사용자들
    user_bank_products = models.ManyToManyField(BankProducts, related_name="bank_product_users")
    join_date = models.DateTimeField()
    expiration_date = models.DateTimeField()
    join_period = models.IntegerField()
    monthly_amount = models.IntegerField()
    interest_rate = models.FloatField()