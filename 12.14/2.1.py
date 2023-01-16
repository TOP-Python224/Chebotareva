from abc import ABC, abstractmethod


# ДОБАВИТЬ везде: строки документации для классов и для не встроенных методов
# ДОБАВИТЬ везде: аннотации типов параметров (кроме self) для всех методов и аннотации типов возвращаемых значений не встроенных методов

# КОММЕНТАРИЙ:
#  основные приёмы использования аннотаций можно найти в документации по модулю typing:
#  https://docs.python.org/3/library/typing.html#module-typing
#  более полная информация находится в документах PEP:
#  https://peps.python.org/
#  аннотациям и их использованию посвящены документы 483, 484 и 585


# пассажирские и грузовые самолёты
class Carrier(ABC):
    @abstractmethod
    def carry_military(self, items):
        # ИСПОЛЬЗОВАТЬ: строка документации позволяет обойтись без инструкции pass в теле функции
        """Выводит в stdout информацию о полезной нагрузке военного самолёта."""

    @abstractmethod
    def carry_commercial(self, items):
        # ИСПОЛЬЗОВАТЬ: документацию функций принято формулировать так, чтобы первое предложение отвечало на вопрос "что делает функция?" — в последующих предложениях при необходимости указываются подробности о работе функции, а также с помощью синтаксиса Sphinx (https://clck.ru/33HPYU) описываются параметры и возвращаемое значение функции
        """Выводит в stdout информацию о полезной нагрузке коммерческого самолёта."""


class Cargo(Carrier):
    # ИСПОЛЬЗОВАТЬ: для классов формулировка строк документации более разнообразна, но, как и в любой документации, первым предложением лучше всего описывать самую суть — в учебных задачах возможны допущения для краткости
    """Реализация грузового самолёта."""

    def carry_military(self, items):
        print("The plane carries ", items," military cargo")

    def carry_commercial(self, items):
        print("The plane carries ", items," commercial cargo")


class Passenger(Carrier):
    def carry_military(self, passengers):
        print("The plane carries ", passengers, " military passengers")

    def carry_commercial(self, passengers):
        print("The plane carries ", passengers, " commercial passengers")


# военные и коммерческие самолёты
class Plane(ABC):
    # ИСПРАВИТЬ здесь и далее: имена всех переменных принято писать в нижнем регистре; к тому же в данном конкретном случае имя параметра Carrier вступает в конфликт с именем класса Carrier — таких ситуаций однозначно лучше избегать
    # КОММЕНТАРИЙ: правилам выбора имён для пользовательских идентификаторов посвящен документ PEP 8
    def __init__(self, Carrier):
        self.carrier = Carrier

    @abstractmethod
    def display_description(self):
        pass

    @abstractmethod
    def add_objects(self):
        pass


class Commercial(Plane):
    def __init__(self, Carrier, objects):
        super().__init__(Carrier)
        self.objects = objects

    def display_description(self):
        self.carrier.carry_commercial(self.objects)

    def add_objects(self, new_objects):
        self.objects += new_objects


class Military(Plane):
    def __init__(self, Carrier, objects):
        super().__init__(Carrier)
        self.objects = objects

    def display_description(self):
        self.carrier.carry_military(self.objects)

    def add_objects(self, new_objects):
        self.objects += new_objects


cargo = Cargo()
passenger = Passenger()

# военный и груз
military1 = Military(cargo, 123)
military1.display_description()
military1.add_objects(12)
military1.display_description()


# ДОБАВИТЬ: после метки stdout закомментированный вывод тестового выполнения кода
# stdout:
