# django-backend-youtube

# 1일차

## 프로젝트 세팅

### 1. Github

- 레포지토리 생성
- 로컬에 있는 내 컴퓨터 폴더와 깃헙의 Remote 공간 연결

### 2. Docker Hub

- 회원가입
- 나의 컴퓨터에 가상환경을 구축 (윈도우, 맥 -> 리눅스 환경 구축(MySQL, Python, Redis)) => 오류 방지를 위해
- AccessToken값을 Github 레포지토리에 등록 => 빌드 목적

### 3. 장고 프로젝트 세팅

- requirements.txt => 실제 배포할 때 사용
- requirements.dev.txt => 개발하고 연습할 때 사용 (파이썬 패키지 관리) DRF 버전업 해볼까? 로컬에서
- 실전 : 패키지 의존성 관리 => 버전관리, 패키지들 간의 관계 관리
    - 장고가 버전이 업데이트 됐는데 내가 가지고 있는 것들과 에러가 나면 안 되니깐