from typing import Union
import doctest


# TODO Написать 3 класса с документацией и аннотацией типов

class Person:
    def __init__(self, gender: str, height: Union[int, float], weight: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Человек"

        :param gender: Пол
        :param height: Рост
        :param weight: Вес
        """

        self.bmi = None
        self.gender = None
        self.height = None
        self.weight = None
        self.init_gender(gender)
        self.init_height(height)
        self.init_weight(weight)

    def init_gender(self, gender):
        if not isinstance(gender, str):
            raise TypeError("Ошибка типа")
        if not gender.lower() in ["мужской", "женский"]:
            raise ValueError("Существует только два пола: male (мужской) или female (женский)")
        self.gender = gender

    def init_height(self, height):
        if not isinstance(height, (int, float)):
            raise TypeError("Ошибка типа")
        if height <= 0:
            raise ValueError("Не верное значения роста")
        self.height = height

    def init_weight(self, weight):
        if not isinstance(weight, (int, float)):
            raise TypeError("Ошибка типа")
        if weight <= 0:
            raise ValueError("Не верное значения веса")
        self.weight = weight

    def __str__(self):
        return f"Пол: {self.gender}, Рост: {self.height} см, Вес: {self.weight} кг"

    def calcul_bmi(self):
        """
        Функция расчета индекса массы тела (ИМТ)
        :return: значение ИМТ
        """
        self.bmi = self.weight / ((self.height / 100) * (self.height / 100))

        if self.bmi <= 16:
            return f"Ваш ИМТ: {self.bmi: .1f}, Выраженный дефицит массы тела. Риск проблем со здоровьем."

        elif 16 < self.bmi < 18.5:
            return f"Ваш ИМТ: {self.bmi: .1f}, Недостаточная (дефицит) масса тела. Риск проблем со здоровьем."

        elif 18.5 < self.bmi < 25:
            return f"Ваш ИМТ: {self.bmi: .1f}, Норма. Риски для здоровья минимальны."

        elif 25 < self.bmi < 30:
            return f"Ваш ИМТ: {self.bmi: .1f}, Избыточная масса тела (предожирение)."

        elif 30 < self.bmi < 35:
            return f"Ваш ИМТ: {self.bmi: .1f}, Ожирение 1 степени. Значительное увеличение рисков для здоровья."

        elif 35 < self.bmi < 40:
            return f"Ваш ИМТ: {self.bmi: .1f}, Ожирение 2 степени. Значительное увеличение рисков для здоровья."

        elif self.bmi > 40:
            return f"Ваш ИМТ: {self.bmi: .1f}, Ожирение 3 степени. Значительное увеличение рисков для здоровья."

        else:
            return f"Что-то, где-то неправильно указали."

    def add_weight(self, new_weight):
        """
        Увеличения веса человека

        :param new_weight: На сколько изменить вес
        :return: Новое значение
        """
        if not isinstance(new_weight, (int, float)):
            raise TypeError("Ошибка типа")
        if new_weight < 0:
            raise ValueError("Не верное значение веса")
        self.weight += new_weight

    def add_height(self, new_height):
        """

        Увеличение роста человека

        :param new_height: На сколько изменить рост
        :return: Новое значение
        """
        if not isinstance(new_height, (int, float)):
            raise TypeError("Ошибка типа")
        if new_height < 0:
            raise ValueError("Не верное значение роста")
        self.height += new_height

    def del_weight(self, new_weight):
        """

        Уменьшение веса человека

        :param new_weight: На сколько изменить вес
        :return: Новое значение
        """
        if not isinstance(new_weight, (int, float)):
            raise TypeError("Ошибка типа")
        if new_weight < 0 or new_weight >= self.weight:
            raise ValueError("Не верное значение веса, значение больше, чем начальный вес человека")
        self.weight -= new_weight

    def del_height(self, new_height):
        """

        Уменьшение роста человека

        :param new_height: На сколько изменить рост
        :return: Новое значение
        """
        if not isinstance(new_height, (int, float)):
            raise TypeError("Ошибка типа")
        if new_height < 0 or new_height >= self.height:
            raise ValueError("Не верное значение роста, значение больше, чем начальный рост человека")
        self.height -= new_height


class Box:

    def __init__(self, length: Union[int, float], width: Union[int, float], height: Union[int, float]):
        """

        Создание и подготовка к работе объекта "Параллелепипед"

        :param length: Длина
        :param width: Ширина
        :param height: Высота
        """
        self.v_par = None
        self.s_pol = None
        self.s_bok = None
        self.s_osn = None
        self.p_osn = None
        self.length = None
        self.width = None
        self.height = None
        self.init_length(length)
        self.init_width(width)
        self.init_height(height)

    def init_length(self, length):
        if not isinstance(length, (int, float)):
            raise TypeError("Ошибка типа")
        if length <= 0:
            raise ValueError("Не верное значение длины")
        self.length = length

    def init_width(self, width):
        if not isinstance(width, (int, float)):
            raise TypeError("Ошибка типа")
        if width <= 0:
            raise ValueError("Не верное значение длины")
        self.width = width

    def init_height(self, height):
        if not isinstance(height, (int, float)):
            raise TypeError("Ошибка типа")
        if height <= 0:
            raise ValueError("Не верное значение высоты")
        self.height = height

    def __str__(self):
        return f"Параллелепипед с размерами: длина : {self.length} см, ширина: {self.width} см, высота: {self.height} см"

    def perimeter_osn(self):
        """
        Периметр основания прямого параллелепипеда
        :return:
        """
        self.p_osn = (self.width * self.length) * 2
        return f"Периметр основания =  {self.p_osn} см"

    def square_bok(self):
        """
        Площадь боковой поверхности прямого параллелепипеда
        :return:
        """
        self.s_bok = (self.p_osn * self.height)
        return f"Площадь боковой поверхности =  {self.s_bok} см\u00B2"

    def square_osn(self):
        """
        Площадь основания прямого параллелепипеда
        :return:
        """
        self.s_osn = self.width * self.length
        return f"Площадь основания = {self.s_osn} см\u00B2"

    def square_pol(self):
        """
        Площадь всей поверхности прямого параллелепипеда
        :return:
        """
        self.s_pol = 2 * self.s_osn + self.s_bok
        return f"Площадь всей поверхности = {self.s_pol} см\u00B2"

    def volume_par(self):
        """
        Объем прямого параллелепипеда
        :return:
        """
        self.v_par = self.s_osn * self.height
        return f"Объем = {self.v_par} см\u00B3"


class Workers:

    def __init__(self, surname: str, name: str, salary: Union[int, float]):
        """

        Создание и подготовка к работе объекта "Работники"

        :param surname: Фамилия
        :param name: Имя
        :param salary: Зарплата

        >>> rab_1 = Workers("Иванов", "Иван", 10000)
        """
        self.surname = None
        self.init_surname(surname)
        self.name = None
        self.init_name(name)
        self.salary = None
        self.init_salary(salary)

    def init_surname(self, surname):
        """
        Функция которая проверяет верность заполнения фамилии. Инициализация.
        :param surname: Фамилия
        :return: TypeError("Ошибка типа")
        """
        if not isinstance(surname, str):
            raise TypeError("Ошибка типа")
        self.surname = surname

    def init_name(self, name):
        """
        Функция которая проверяет верность заполнения имени. Инициализация.
        :param name: Имя
        :return: TypeError("Ошибка типа")
        """
        if not isinstance(name, str):
            raise TypeError("Ошибка типа")
        self.name = name

    def init_salary(self, salary):
        """
        Функция которая проверяет верность заполнения значения з/п. Инициализация.
        :param salary: Значение з/п
        :return: TypeError("Ошибка типа")
        """
        if not isinstance(salary, (int, float)):
            raise TypeError("Ошибка типа")
        if salary <= 0:
            raise ValueError("Не верное значения зарплаты. Не может быть равно нулю и быть отрицательной")
        self.salary = salary

    def __str__(self):
        """
        Функция для отображения в пользовательском виде
        :return: F - строку
        """
        return f"Фамилия: {self.surname}\nИмя: {self.name}\nЗарплата: {self.salary}"

    def add_salary(self, new_salary):
        """
        Функция увеличения зарплаты
        :param new_salary: на сколько увеличить з/п
        :return: Новое значение

        >>> rab_1 = Workers("Иванов", "Иван", 10000)
        >>> rab_1.add_salary(500)
        >>> rab_1 = Workers("Иванов", "Иван", 10500)
        """
        if not isinstance(new_salary, (int, float)):
            raise TypeError("Ошибка типа")
        if new_salary < 0:
            raise ValueError("Не верное значение зарплаты")
        self.salary += new_salary

    def del_salary(self, new_salary):
        """
        ункция уменьшения з/п
        :param new_salary: на сколько уменьшить з/п
        :return: Новое значение з/п

        >>> rab_1 = Workers("Иванов", "Иван", 10000)
        >>> rab_1.del_salary(500)
        >>> rab_1 = Workers("Иванов", "Иван", 9500)
        """
        if not isinstance(new_salary, (int, float)):
            raise TypeError("Ошибка типа")
        if new_salary < 0 or new_salary >= self.salary:
            raise ValueError("Значение не может быть больше, чем начальное значение")
        self.salary -= new_salary


if __name__ == "__main__":
    print("--- Класс Человек ---")
    person_1 = Person("Мужской", 178, 80)
    person_2 = Person("Женский", 160, 58)
    print(person_1)
    print(person_2)
    print(person_1.calcul_bmi())
    print(person_2.calcul_bmi())
    print("Изменяем вес первого человека...")
    person_1.add_weight(20)
    print(person_1)
    print("Изменяем вес первого человека...")
    person_1.del_weight(20)
    print(person_1)
    print("--- Класс Коробка ---")
    box_1 = Box(25, 30, 15)
    print(box_1)
    print(box_1.perimeter_osn())
    print(box_1.square_bok())
    print(box_1.square_osn())
    print(box_1.square_pol())
    print(box_1.volume_par())
    print("--- Класс Работник ---")
    worker_1 = Workers("Иванов", "Иван", 10000)
    worker_2 = Workers("Иванова", "Светлана", 9000)
    print(worker_1)
    print(worker_2)
    print("Изменяем з/п первого работника...")
    worker_1.del_salary(500)
    print(worker_1)
    print("Изменяем з/п второго работника...")
    worker_2.add_salary(1000)
    print(worker_2)
    doctest.testmod()  # тестирование примеров, которые находятся в документации

    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
