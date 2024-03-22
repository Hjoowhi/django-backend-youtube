from rest_framework import serializers
from .models import Video
from users.serializers import UserSerializer
from comments.serializers import CommentSerializer

class VideoListSerializer(serializers.ModelSerializer):

    # Video:User => Video(FK) -> User
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Video
        fields = '__all__'
        # depth = 1


from reactions.models import Reaction
class VideoDetailSerializer(serializers.ModelSerializer):

    # Video:User => Video(FK) -> User
    user = UserSerializer(read_only=True) # 유저를 읽어줄 시리얼라이저

    # Video:Comment => Video -> Comment(FK)
    # - Reverse Accessor
    # - 부모가 자녀를 찾을 때 => _set을 붙이면 부모에 속한 자녀들을 모두 찾을 수 있다.
    comment_set = CommentSerializer(many=True, read_only=True) # 비디오 만들 때 댓글 정보는 필요없어서

    reactions = serializers.SerializerMethodField()
    
    class Meta:
        model = Video
        fields = '__all__'
        # depth = 1

    # Reaction 데이터 받아보기
    def get_reactions(self, video):
        return Reaction.get_video_reaction(video) # video 줄게, reaction 줘(return)