from django.db import models
from common.models import CommonModel
from django.db.models import Count, Q

# - User : FK
# - Video : FK
# - reaction (like, dislike, cancel) => choice (케이스 정해주기) : circular error 방지

# 좋아요, 싫어요 갯수를 불러와야 한다. => Video REST API

class Reaction(CommonModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)

    LIKE = 1
    DISLIKE = -1
    NO_REACTION = 0

    REACTION_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
        (NO_REACTION, 'No Reaction')
    )

    reaction = models.IntegerField(
        choices=REACTION_CHOICES,
        default=NO_REACTION
    )

    # ORM depth2 -> SQL : JOIN 쿼리와 비슷
    # 좋아요, 싫어요 숫자 세기
    @staticmethod
    def get_video_reaction(video):
        # reaction 테이블에서 video가 같은 걸 조회하는 게 더 쉽다. -> reaction 먼저 부르는 이유
        reactions = Reaction.objects.filter(video=video).aggregate(
            likes_count = Count('pk', filter=Q(reaction=Reaction.LIKE)), # filter를 걸 때는 Q() 함수 필요
            dislikes_count = Count('pk', filter=Q(reaction=Reaction.DISLIKE)),
        )

        return reactions