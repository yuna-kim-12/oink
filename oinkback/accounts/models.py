from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

# 커스텀 유저 매니저: 이메일을 기본 식별자로 사용하는 유저 생성 관리
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

# 커스텀 유저 모델: AbstractUser를 상속받아 이메일 기반 인증 구현
class User(AbstractUser):
    # username 필드 제거 (이메일을 기본 식별자로 사용)
    username = None
    # 필수 필드 정의
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=10)
    birth_date = models.DateField()
    saving_purpose = models.JSONField()  # 다중 선택을 위해 JSONField 사용
    saving_amount = models.IntegerField()
    saving_period = models.IntegerField()

    # 이메일을 username 대신 식별자로 사용
    USERNAME_FIELD = 'email'
    # 필수로 입력받을 필드 목록
    REQUIRED_FIELDS = ['name', 'birth_date', 'saving_purpose', 'saving_amount', 'saving_period']

    objects = CustomUserManager()

    def __str__(self):
        return self.email