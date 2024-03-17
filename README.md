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