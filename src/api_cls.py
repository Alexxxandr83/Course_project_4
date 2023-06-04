from abc import ABC, abstractmethod
import requests


class AbstractApiClass(ABC):
    """Обязывает создать метод получения вакансии для каждого сайта отдельно"""

    @abstractmethod
    def get_vacancies(self):
        pass


class HH_API(AbstractApiClass):
    """Получаем данные с hh.ru"""

    def get_vacancies(self):

        url = 'https://api.hh.ru/vacancies'
        params = {'area': 1, 'text': 'python',
                  'per_page': 10}

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            vacancies = []
            for item in data['items']:
                salary = item.get('salary', {})
                vacancies.append(
                    Vacancy(
                        name=item['name'],
                        url=item['url'],
                        description=item['snippet']['requirement'],
                        salary_to=salary.get('to') if salary is not None else None,
                        salary_from=salary.get('from') if salary is not None else None
                    )
                )
            return vacancies
        else:
            print('Ошибка при запросе данных о вакансиях')
            return None
