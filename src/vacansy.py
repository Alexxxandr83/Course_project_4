class Vacancy:
    """
    Класс для работы с вакансиями, реализован для получения нужных объектов
    """

    def __init__(self, name: str, url: str, salary_to: int, salary_from: int, description: str):
        self.name = name
        self.url = url
        self.salary_to = salary_to
        self.salary_from = salary_from
        self.description = description

    def __str__(self):
        """
        Возвращает строковое представление объекта класса vacancy.
        :return: str
        """
        return f"Vacancy: {self.name}\nURL: {self.url}\nSalaryTo: {self.salary_to}\n" \
               f"SalaryFrom: {self.salary_from}\nDescription: {self.description}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        """
        Позволяет реализовать проверку на равенство для экземпляров пользовательских типов.
        :param other: vacancy - экземпляр класса Vacancy
        :return: bool
        """
        return self.salary_to == other.salary

    def __lt__(self, other):
        """
        Позволяет реализовать проверку на «меньше чем» для экземпляров пользовательских типов.
        :param other: vacancy - экземпляр класса vacancy
        :return: bool
        """
        return self.salary_to < other.salary
