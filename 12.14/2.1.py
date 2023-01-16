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
        # ИСПОЛЬЗОВАТЬ: следите за символами пространства, когда работаете со строками — у функции print() есть параметр sep со значением по умолчанию ' ', во время формирования итоговой строки для записи в stdout он подставляется между всеми аргументами, передаваемыми функции
        print("The plane carries", items, "military cargo")

    def carry_commercial(self, items):
        print("The plane carries", items, "commercial cargo")


class Passenger(Carrier):
    def carry_military(self, passengers):
        print("The plane carries", passengers, "military passengers")

    def carry_commercial(self, passengers):
        print("The plane carries", passengers, "commercial passengers")


# военные и коммерческие самолёты
class Plane(ABC):
    # ИСПРАВИТЬ здесь и далее: имена всех переменных принято писать в нижнем регистре; к тому же в данном конкретном случае имя параметра Carrier вступает в конфликт с именем класса Carrier — таких ситуаций однозначно лучше избегать
    # КОММЕНТАРИЙ: правилам выбора имён для пользовательских идентификаторов посвящен документ PEP 8
    def __init__(self, Carrier):
        self.carrier = Carrier

    @abstractmethod
    # ИСПРАВИТЬ здесь и далее: сигнатура абстрактного метода должна соответствовать сигнатурам всех реализаций этого метода, и наоборот — это значит, что при объявлении абстрактного метода необходимо перечислить все параметры, которые должны использовать реализации
    def display_description(self):
        pass

    # КОММЕНТАРИЙ: это необходимо для того, чтобы второй разработчик, пишущий свой класс, наследующий от абстрактного класса, написанного первым разработчиком, точно знал какие методы он должен реализовать — потому что классы-наследники второго разработчика могут быть использованы в коде первого или третьих разработчиков

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

# ДОБАВИТЬ: больше тестов


# ДОБАВИТЬ: после метки stdout закомментированный вывод тестового выполнения кода
# stdout:


# ИТОГ: в том, что касается Моста, всё хорошо — 5/6


# СДЕЛАТЬ: совершенно напрасно вы игнорируете лекцию, посвящённую работе с git и GitHub — не нужно пытаться использовать GitHub также, как файлообменник Teams — это мизер и того не стоит: используйте преимущества систем версификации, такие как клонирование удалённого репозитория, систему коммитов, их историю и так далее — потраченное на просмотр лекции время окупится меньше чем за месяц

# СДЕЛАТЬ: описания коммитов (commit message) должны передавать содержание коммита, а не бессмысленное "Add files via upload" или "ДЗ" — берите пример с моих сообщений