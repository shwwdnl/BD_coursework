import psycopg2.errors

from fill_database import ConnectDB


class TablesCreator:
    """Класс для создания таблиц в PosgreSQL"""

    @staticmethod
    def create_employers(table_name: str):
        """Метод для создания таблиц с работодателями"""
        conn = ConnectDB.connect_to_db()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(f"""CREATE TABLE {table_name}
                                (employer_id int PRIMARY KEY, 
                                employer_name varchar(100), 
                                employer_url varchar(200))""")
        except psycopg2.errors.DuplicateTable:
            print(f"Таблица с таким именем найдена, считываю данные")
        finally:
            conn.close()

    @staticmethod
    def create_vacancies(table_name: str):
        """Метод для создания таблиц с вакансиями"""
        conn = ConnectDB.connect_to_db()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(
                        f"""CREATE TABLE {table_name} 
                        (vacancy_id int PRIMARY KEY, 
                        vacancy_name varchar(100), 
                        vacancy_url varchar(200), 
                        vacancy_salary_from int, 
                        vacancy_salary_to int, 
                        employer_id int 
                        REFERENCES employers(employer_id));""")
        except psycopg2.errors.DuplicateTable:
            print(f"Таблица с таким именем найдена, считываю данные")
        finally:
            conn.close()