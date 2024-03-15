# Django가 DB 연결에 실패했을 시, 재시도를 하도록 만드는 로직을 추가
from django.core.management.base import BaseCommand
from django.db import connections
import time

# Operation Error & Psycopg2 Operation Error
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OpError

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for DB connenction ...')

        is_db_connected = None
        while not is_db_connected: # DB 연결이 아닐 때까지 시도
            try:
                is_db_connected = connections['default'] # app/settings.py의 DATABASES의 'default'
            except (OperationalError, Psycopg2OpError):
                self.stdout.write('Retrying DB connection ...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('PostgreSQL DB Connection Success'))