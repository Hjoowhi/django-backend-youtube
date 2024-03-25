from django.urls import path

websocket_urlpatterns = [
    path('ws/chat/<int:room_id>/') # ws/chat/{room_id} => 룸 넘버에 따라 채팅 구분
]