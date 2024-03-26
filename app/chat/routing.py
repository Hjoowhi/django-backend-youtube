from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/chat/<int:room_id>/', ChatConsumer.as_asgi()) # ws://ws/chat/{room_id} => 룸 넘버에 따라 채팅 구분
]