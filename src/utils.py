import json


def get_top_n_vacancies(filename: str, n: int):
    """Сортирует вакансии по значению зарплаты от наивысшей до наименьшей"""
    with open(filename, 'r', encoding='utf-8') as file:
        vacancies = json.load(file)

    sorted_vacancies = sorted(vacancies, key=lambda x: x.get('salary_from', 0) or 0, reverse=True)
    filtered_vacancies = [v for v in sorted_vacancies if v.get('salary_from') is not None and v.get('salary_from') > 0]

    return filtered_vacancies[:n]

