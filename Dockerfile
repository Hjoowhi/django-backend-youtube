# 도커 이미지 구축
# alpine: Linux 경량화
# Alpine Linux는 경량화된 리눅스 배포판으로, 컨테이너 환경에 적합
# Python 3.11이 설치된 Alpine Linux 3.19
FROM python:3.11-alpine3.19

# LABEL 명령어는 이미지에 메타데이터를 추가합니다. 
# 여기서는 이미지의 유지 관리자를 "joowhi"로 지정하고 있습니다.
LABEL maintainer='joowhi'

# 환경 변수 PYTHONUNBUFFERED를 1로 설정합니다. 
# 이는 Python이 표준 입출력 버퍼링을 비활성화하게 하여, 로그가 즉시 콘솔에 출력되게 합니다. 
# => 파이썬 관련 로그를 확인할 수 있게 해주는 옵션 (기본값은 0=False)
# 이는 Docker 컨테이너에서 로그를 더 쉽게 볼 수 있게 합니다.
ENV PYTHONUNBUFFERED 1

# 로컬 파일 시스템의 requirements.txt 파일을 컨테이너의 /tmp/requirements.txt로 복사합니다. 
# => 로컬에서 작업한 파일들을 가상환경으로 복사하는 코드
# 이 파일은 필요한 Python 패키지들을 명시합니다.
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false

# 리눅스 -> venv 설치
# && \ : 엔터치는 거랑 같다고 생각
# 파이썬의 가상 환경을 /py 디렉토리에 생성한다. 
# (가상환경 사용 시, 시스템의 파이썬 환경과 독립적으로 패키지 관리를 할 수 있음)
RUN python -m venv /py && \
    # 가상환경 내 pip(파이썬 패키지 관리자)를 최신 버전으로 업그레이드
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    # 필수 파이썬 패키지들을 명시된 파일(requirements.txt)에 설치
    /py/bin/pip install -r /tmp/requirements.txt && \
    # DEV 환경 변수가 true로 설정되어 있는지 확인 -> 개발용 의존성이 설치될지를 결정한다 (띄어쓰기 필수)
    if [ $DEV = "true" ]; \
        # true일 경우, 개발용 의존성을 담고 있는 파일(requirements.dev.txt)에 명시된 추가 패키지들 설치
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    # 조건문 끝
    fi && \
    # /tmp 디렉토리를 삭제하여 빌드 중 생성된 임시 파일들 정리 -> 이미지의 크기를 줄이는 데 도움이 된다.
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    # 새로운 사용자 추가 -> 보안상의 이유로 root 사용자가 아닌 일반 사용자 권한으로 실행하는 것이 좋다.
    adduser \
        # 생성되는 사용자에게 패스워드를 설정하지 않는다. (우선 이 프로젝트에서 내가 하는데 당장은 번거로우니깐)
        --disabled-password \
        # 사용자의 홈 디렉토리를 생성하지 않는다.
        --no-create-home \
        # 생성할 사용자 이름
        django-user

# 환경 변수 PATH를 설정하여, 가상 환경의 Python과 스크립트 디렉토리에서 실행 가능한 파일들을 쉽게 찾을 수 있도록 한다.
ENV PATH="/py/bin:$PATH"

USER django-user