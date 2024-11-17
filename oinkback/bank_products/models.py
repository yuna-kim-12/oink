from django.db import models

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
    join_amount_max = models.IntegerField(null=True)
    join_amount_text = models.TextField()
    join_way = models.TextField(null=True)
    join_member = models.TextField()
    prime_conditions = models.TextField(null=True)
    interest_payment = models.TextField(null=True)
    note = models.TextField(null=True)