from django.db import models
from common.models import CommonModel

# ChatRoom 모델을 분리했을 때의 이점
# - 관리의 용이
# - 확장성 (채팅방: 오픈채팅방, 업무채팅방-비밀번호를 입력해야 들어갈 수 있음) ★★★
class ChatRoom(CommonModel):
    name = models.CharField(max_length=100)


class ChatMessage(CommonModel):
    # SET_NULL - sender null 값으로 두겠다. 1번 유저 -> 계정 삭제 -> null
    sender = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True) # 참조하는 외래키 알 수 없음으로 나타내기 -> 유저가 계삭해도 채팅은 남아있으니깐
    message = models.TextField()
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

# User:Msg(FK) => 1:N
    # => User: Msg, Msg, ... (O)
    # => Msg: User, User, ... (X)

# Room(부모) - Msg(자녀)
# Room:Msg(FK) => 1:N
    # - Room: Msg, Msg, ... => (O)
    # - Msg: Room, Room, ... => (X)