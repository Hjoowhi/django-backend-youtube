from django.db import models
from common.models import CommonModel
from users.models import User

# - User : FK => subscriber (내가 구독한 사람)
# - User : FK => subscribed_to (나를 구독한 사람)

# User:Subscription => 
    # User(subscriber) => subscriber, subscriber, subscriber, ... (O) -> FK
    # User(subscribed_to) => subscribed_to, subscribed_to, subscribed_to, ... (O) -> FK

class Subscription(CommonModel):
    # 내가 구독한 유튜버
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions') # 유튜버가 채널을 삭제했을 때, 구독자들도 삭제되어야 한다.

    # 나를 구독한 사람
    subscribed_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers') # 구독자 한 명이 채널을 삭제하면, 내 구독자 수가 한 명 줄어든다. (만 명 -> 9999명)

    # related_name을 사용하면 subscriber_set으로 안 하고 저기서 지정한 subscriptions로 불러올 수 있다.
        # subscriber_set으로 -> subscriptions
        # subscribed_to_set -> subscribers
