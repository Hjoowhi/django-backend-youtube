from django.shortcuts import render
from rest_framework.views import APIView
from .models import Video
from .serializers import VideoListSerializer, VideoDetailSerializer

from rest_framework.response import Response
from rest_framework import status

# Video와 관련된 REST API

# 1. VideoList
# 전체 데이터 컨트롤
# api/v1/video
# [GET] : 전체 비디오 목록 조회
# [POST] : 새로운 비디오 생성
# [PUT] : X
# [DELETE] : X

class VideoList(APIView):
    def get(self, request):
        videos = Video.objects.all() # QuerySet[Video, Video, Video, ....]

        # 직렬화 (Object -> Json) - Serializer(내가 원하는 데이터만 내려주는)
        serializer = VideoListSerializer(videos, many=True) # 쿼리셋 안 데이터가 2개 이상일 때 many=True

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user_data = request.data # Json -> Object(역직렬화)
        serializer = VideoListSerializer(data=user_data) # 데이터를 바로 넣으려면 data= 이 있어야 한다.

        if serializer.is_valid():
            serializer.save(user=request.user) # save 함수를 사용하면 대부분 어떤 유저가 하는지 명시해주는 게 좋다.
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 디버깅을 위해 실패할 경우도 표시해주기!


# 2. VideoDetail
# 개별 데이터 컨트롤
# api/v1/video/{video_id}
# [GET] : 특정 비디오 조회
# [POST] : X
# [PUT] : 특정 비디오 업데이트
# [DELETE] : 특정 비디오 삭제

from rest_framework.exceptions import NotFound

class VideoDetail(APIView): # APIView : GET, PUT, DELETE 구분
    def get(self, request, pk):
        try:
            video = Video.objects.get(pk=pk)
        except:
            raise NotFound
        
        serializer = VideoDetailSerializer(video) # Object -> Json

        return Response(serializer.data)

    def put(self, request, pk):
        video_obj = Video.objects.get(pk=pk) # DB에서 불러온 데이터
        user_data = request.data # 유저가 보낸 데이터
        
        serializer = VideoDetailSerializer(video_obj, user_data) # video_obj를 user_data로 시리얼라이즈(변경)해 주세요.
        
        serializer.is_valid(raise_exception=True) # is_valid() 함수를 실행해야 save() 함수가 실행된다.
        serializer.save() # 실제 저장 

        return Response(serializer.data)

    def delete(self, request, pk):
        video_obj = Video.objects.get(pk=pk)
        video_obj.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)