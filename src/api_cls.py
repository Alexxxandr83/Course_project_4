from abc import ABC, abstractmethod


class AbstractApiClass(ABC):
    """Обязывает создать метод получения вакансии для каждого сайта отдельно"""

    @abstractmethod
    def get_vacancies(self):
        pass
