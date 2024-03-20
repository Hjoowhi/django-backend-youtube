from rest_framework import serializers
from .models import Video
from users.serializers import UserSerializer
from comments.serializers import CommentSerializer

class VideoSerializer(serializers.ModelSerializer):

    # 유저를 읽어줄 시리얼라이저
    user = UserSerializer(read_only=True) # Video(FK)
    comment = CommentSerializer(read_only=True)
    
    class Meta:
        model = Video
        fields = '__all__'
        # depth = 1