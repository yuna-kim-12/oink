from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # email 중복되지 않게 가입: unique
    email = models.EmailField(max_length=100, unique=True)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    age = models.IntegerField()
    saving_purpose = models.TextField()
    saving_amount = models.IntegerField()
    saving_period = models.IntegerField()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []