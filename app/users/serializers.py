from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    # 내려줄 모델과 필드 정의
    class Meta:
        model = User
        fields = ('id', 'email', 'nickname', 'is_business')