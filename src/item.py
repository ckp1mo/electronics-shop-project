import csv
from src.InstantiateCSVError import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
        super().__init__()

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        """
        Складываем количество товара из родительских или дочерних экземпляров
        """
        if not issubclass(other.__class__, self.__class__):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        """
        Проверка длины имени и если больше 10 символов, то режет
        """
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[0:10]

    @classmethod
    def instantiate_from_csv(cls, file):
        """
        Собирает экземпляры класса на основе содержимого файла csv.
        Очищает список ранее добавленных экземпляров
        """
        Item.all.clear()
        try:
            with open(file, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if len(row) < 3:
                        raise InstantiateCSVError
                    name = row['name']
                    price = int(row['price'])
                    quantity = int(row['quantity'])
                    cls(name, price, quantity)
        except FileNotFoundError:
            print('Отсутствует файл items.csv')
        except InstantiateCSVError as ex:
            print(ex.message)

    @staticmethod
    def string_to_number(str_number):
        """
        Переводит строковое значение в числовое, отбросив цифры после точки
        """
        return int(float(str_number))
