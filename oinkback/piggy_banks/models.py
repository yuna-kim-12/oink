from django.db import models
from django.conf import settings
# 아직 윤하언니 커밋 전
# from bank_products.models import UserProduct


# Create your models here.
class PiggyBank(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    # 아직 윤하언니 커밋 전
    # user_product = models.ForeignKey(UserProduct, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    weight = models.FloatField(default=0.0)
    cheerup_count = models.IntegerField(default=0)