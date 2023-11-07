from DB_manager.create_tables import TablesCreator
from DB_manager.fill_database import FillDB
from DB_manager.BD_manager import DBManager


def main():
    """Код для проверки работоспособности программы"""
    employers = ['skyeng', 'Яндекс', 'Тинькофф', 'lesta games', 'VK', 'LG Electronics Inc.',
                 'SberTech', 'YADRO', 'Альфа-Банк', 'GeekBrains']
    user_input_emp = input("Введите имя таблицы с работодателями: ")
    tables_creator = TablesCreator
    tables_creator.create_employers(user_input_emp)
    user_input_vac = input("Введите имя таблицы с вакансиями: ")
    tables_creator.create_vacancies(user_input_vac)
    print(f"""Программа позволяет ознакомиться с информацией по наличию вакансий у следующих
работодателей {', '.join(employers)}""")
    fill_db = FillDB(employers)
    fill_db.fill_db_employers(user_input_emp)
    try:
        fill_db.fill_db_vacancies(user_input_vac)
    except TypeError:
        print("Данные не получены")
    db_manager = DBManager
    data = db_manager.get_companies_and_vacancies_count(user_input_emp, user_input_vac)
    for d in data:
        print(d)
    all_info = db_manager.get_all_vacancies(user_input_emp, user_input_vac)
    for info in all_info:
        print(info)
    salary = db_manager.get_avg_salary(user_input_vac)
    print(salary)
    top_salary = db_manager.get_vacancies_with_higher_salary(user_input_vac)
    for top in top_salary:
        print(top)
    vacancies = db_manager.get_vacancies_with_keyword(user_input_vac, "Python")
    for vac in vacancies:
        print(vac)


if __name__ == "__main__":
    main()