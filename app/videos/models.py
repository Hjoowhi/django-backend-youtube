from django.db import models
from common.models import CommonModel
from users.models import User

class Video(CommonModel):
    title = models.CharField(max_length=30) # 제목이 너무 길면 조금 그러니 제한 두기
    description = models.TextField(blank=True) # 내용이 없을 수도 있음
    link = models.URLField()
    category = models.CharField(max_length=20)
    views_count = models.PositiveIntegerField(default=0) # 조회수가 음수인 건 이상하니깐
    thumbnail = models.URLField() # S3 Bucket -> Save File -> URL -> Save URL
    video_file = models.FileField(upload_to='storage/') # 파일을 저장하는 방법

    user = models.ForeignKey(User, on_delete=models.CASCADE)

# User:Video  => 1:N (자녀가 KEY를 가진다. -> Video가 FK를 가진다.)
    # => User : Video, Video, Video ... -> O
    # => Video : User, User, User (유튜버 3명이 찍은 영상) -> X -> 가능할 때 다시 기능 변경해주면 됨

# docker-compose run --rm run sh -c 'python manage.py makemigration'
    # makemigration => 장고한테 알려주는 것
    # migrate => 장고가 DB 찾아가는 것