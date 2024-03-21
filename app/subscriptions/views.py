from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SubSerializer
from .models import Subscription
from django.shortcuts import get_object_or_404
from rest_framework import status

# 구독과 관련한 REST API

# SubscriptionList
# api/v1/subscription
# [GET] : pk = 나 자신. (pk 입력받을 필요 X) -> 내가 구독한 유튜브 리스트는 여기서 구현하면 된다! (내가 구독한)
# [POST] : 구독 하기
class SubscriptionList(APIView):
    def post(self, request):
        user_data = request.data # json -> object (Serializer)

        serializer = SubSerializer(data=user_data)

        serializer.is_valid(raise_exception=True)
        serializer.save(subscriber=request.user)

        return Response(serializer.data, 201)

# SubscriptionDetail
# api/v1/subscription/{user_id}
# [GET] : 특정 유저의 구독자 리스트 조회
# [DELETE] : 구독 취소
class SubscriptionDetail(APIView):
    def get(self, request, pk):
        # 나를 구독한 사람들
        # api/v1/sub/{pk} ->  1번 유저가 구독한 사함들의 리스트가 궁금한 것
        subs = Subscription.objects.filter(subscribed_to=pk) # object -> json
        serializer = SubSerializer(subs, many=True)

        return Response(serializer.data) # 200

    # api/v1/sub/{pk}
    def delete(self, request, pk):
        sub = get_object_or_404(Subscription, pk=pk, subscriber=request.user) # 구독 취소한 사람 누군지 알기
        sub.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)