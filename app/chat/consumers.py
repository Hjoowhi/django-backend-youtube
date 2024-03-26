from channels.generic.websocket import AsyncWebsocketConsumer
import json

# Consumer Class : Websocket 연결을 처리하는 부분 
# channel_layer 안에 group 단위로 (Socket 연결)
class ChatConsumer(AsyncWebsocketConsumer):
    # 소켓 연결
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id'] # url_route의 kwargs에서 room_id를 가져온다.
        self.room_group_name = 'chat_' + str(self.room_id)

        # 1. 얘 연결이 끝나면
        await self.channel_layer.group_add(self.room_group_name, self.channel_name) # 그룹으로 묶어줘서 나중에 인원 상관없이 그룹에 있는 사람들은 채팅을 할 수 있다.
        # 2. 얘를 실행해 줘
        await self.accept() # 채널 연결

    # 양방향 - 데이터 실시간 소통 통로
    async def receive(self, text_data):
        data_json = json.loads(text_data) # {'payload':data, 'status':data, ...} : json 형태
        msg = data_json.get('message')

        await self.channel_layer.group_send(self.room_group_name, {
            'type': 'chat_message',
            'message': msg
        })

    # 연결 해제 메서드: 클라이언트의 웹소켓 연결이 끊어졌을 때 호출됩니다.
	# group_discard: 클라이언트를 채팅방 그룹에서 제거합니다. 이를 통해 더 이상 메시지를 받지 않게 됩니다. 
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def chat_message(self, event):
        msg = event['message']
        # email = event['email']

        await self.send(text_data=json.dumps({
            'type': 'chat.message',
            'message': msg
            # 'email': email
        }))