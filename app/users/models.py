from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager)

class UserManager(BaseUserManager):
    # 일반 유저 셍성
    def create_user(self, email, password):
        if not email:
            raise ValueError("Please enter your email address")
        
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        
        return user # django orm

    # 슈퍼 유저 셍성
    def create_superuser(self, email, password):
        user = self.create_user(email, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

# createsuperuser -> email(option), username(required), password
# - email
# - password
# - nickname
# - is_business: personal. business
class User(AbstractBaseUser, PermissionsMixin):
    # CharField => VARCHAR : 가변성 (최대값 안에서 자유로이)
    email = models.CharField(max_length=255, unique=True)
    nickname = models.CharField(max_length=255)
    is_business = models.BooleanField(default=False)

    # PermissionMixin : 권한 관리
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    # 유저를 생성 및 관리 (유저를 구분해서 관리하기 위해 - 관리자계정, 일반계정)
    # 인스턴스 ->  함수를 호출할 때는 self 불필요
    objects = UserManager()

    def __str__(self) -> str:
        return f'email : {self.email}, nickname : {self.nickname}'