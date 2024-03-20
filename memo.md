# django-backend-youtube

# 1일차

## 프로젝트 세팅

### 1. Github

- 레포지토리 생성 (django-backend-youtube)
- 로컬에 있는 내 컴퓨터 폴더와 깃헙의 Remote 공간 연결

### 2. Docker Hub

- 도커 허브 회원가입
- 나의 컴퓨터에 가상환경을 구축 (윈도우, 맥 -> 리눅스 환경 구축(MySQL, Python, Redis)) => 오류 방지를 위해
- AccessToken값을 Github 레포지토리에 등록 => 빌드 목적
    - Github repository -> Settings -> Secrets and vatiables -> Actions -> New repository secret
    - DOCKER_USER -> 도커허브에 설정된 네임
    - DOCKERHUB_TOKEN -> AccessToken 값

### 3. 장고 프로젝트 세팅

- requirements.txt => 실제 배포할 때 사용
- requirements.dev.txt => 개발하고 연습할 때 사용 (파이썬 패키지 관리) DRF 버전업 해볼까? 로컬에서
    - 실전 : 패키지 의존성 관리 => 버전관리, 패키지들 간의 관계 관리
    - 장고가 버전이 업데이트 됐는데 내가 가지고 있는 것들과 에러가 나면 안 되니깐

- Dockerfile
    - 도커 이미지를 구축하기 위한 지시사항을 포함한다.
    - 파이썬 환경을 설정하고 필요한 패키지를 설치한다.

- app 폴더 생성

- .dockerignore 파일 만들고 보안이 필요한 파일 넣어주기

- 단일 도커 이미지 빌드하기 (docker build .)

주말공부
- 도커 배운 것 정리
- 유튜브 데이터베이스 모델 구조 고민해오기
    - user : username(charified)
    - 구독은 어떻게 하지? 좋아요는? 싫어요는? 어디에 담지? 비디오는? 댓글은?

Obstacles are what you see when you take your eyes off your vision

컴퓨터 공학 -> 출발점이 인문학(생각)에 시작
실리콘 밸리 생각 전쟁
- Think Big
- Think Week (MS)
- Think Different (Apple)

개발자 관련 책
- 구루가 된 개발자들

퀀트 자동 투자

## Youtube API 개발
### 1. 모델(테이블) 구조

(1) User => O

- email
- password
- nickname
- is_business(boolean): personal, business

(2) Video => -ing

- title
- link
- description
- category
- views_count
- thumbnail

- User : ForiegnKey

(3) Reaction

- User : FK
- Video : FK
- reaction (like, dislike, cancel)

<!-- (4) Notifications (알림 관련)
- User : FK
- Vidoe : FK

```
User:Notification => 
User -> Noti, Noti, Noti (알림을 여러 개 받을 수 있다.)
Noti -> User (여러 유저에게 보낼 수는 있지만, 여러 유저를 담아서 보낼 수는 없다. OOO님이 신청하신 어쩌구는 가능한데, OOO님, XXX님, AAA님들이 신청하신~ 이렇게 되지는 않음)
```
```
Video:Noti
``` -->

(4) comment
- User : FK
- Video : FK
- content
- like
- dislike

(5) Subscription (채널 구독 관련)
- User : FK => subscriber (내가 구독한 사람)
- User : FK => subscribed_to (나를 구독한 사람)

<!-- 올린 날짜/수정 날짜 -->
(6) Common
- cretaed_at
- updated_at

만들어야 하는 테이블(모델)
- users, videos, reactions, comments, subscriptions, common
- docker-compose run --rm app sh -c 'python manage.py startapp users'
- docker-compose run --rm app sh -c 'python manage.py startapp videos'
- docker-compose run --rm app sh -c 'python manage.py startapp reactions'
- docker-compose run --rm app sh -c 'python manage.py startapp comments'
- docker-compose run --rm app sh -c 'python manage.py startapp subscriptions'
- docker-compose run --rm app sh -c 'python manage.py startapp common'

### Custom User Model Create

- TDO => 개발 및 디버깅 시간을 엄청나게 줄일 수 있다. PDB(Python Debugger)

# DRF 세팅
- DjangoRestframeework
- drf-spectacular => swagger-ui, redoc을 통해 소통 / requirement.txt 추가
- docker-compose build