import psycopg2

from django.core.management import BaseCommand

from config.settings import DATABASE, USER, PASSWORD, HOST, PAD_DATABASE, PORT


class Command(BaseCommand):
    """Создание БД"""

    def handle(self, *args, **options):
        # ConnectionString = f'''PORT={PORT};
        #                        SERVER={HOST};
        #                        DATABASE={PAD_DATABASE};
        #                        UID={USER};
        #                        PWD={PASSWORD}'''
        conn_params = {
            'dbname': PAD_DATABASE,
            'user': USER,
            'password': PASSWORD,
            'host': HOST,
            'port': PORT
        }
        try:
            conn = psycopg2.connect(**conn_params)
        except psycopg2.ProgrammingError as ex:
            print(ex)
        else:
            conn.autocommit = True
            try:
                cursor = conn.cursor()
                cursor.execute(fr'DROP DATABASE {DATABASE};')
            except psycopg2.ProgrammingError as ex:
                print(ex)
            else:
                print(f'База данных {DATABASE} успешно удалена!')
