import psycopg2

from django.core.management import BaseCommand

from config.settings import DATABASE, USER, PASSWORD, HOST, PAD_DATABASE, PORT


class Command(BaseCommand):
    """Проверка подключения к БД"""

    def handle(self, *args, **options):
        try:
            conn = psycopg2.connect(
                dbname=PAD_DATABASE,
                user=USER,
                password=PASSWORD,
                host=HOST,
                port=PORT
            )
            print("Подключение успешно!")
        except Exception as e:
            print("Ошибка подключения:", e)

