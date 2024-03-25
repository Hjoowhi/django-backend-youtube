from .models import ChatRoom, ChatMessage
from rest_framework.serializers import ModelSerializer

class ChatRoomSerializer(ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = '__all__' # 전체로 불러오고 나중에 제외하기

class ChatMessageSerializer(ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'
        read_only_fields = ['room', 'sender']
        depth = 1 # 유저에 대한 정보도 받아보기