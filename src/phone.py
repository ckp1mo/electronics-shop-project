from src.item import Item


class Phone(Item):
    """
    Класс добавляет поле с наличием сим-карт.
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim
        if self.__number_of_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, sim):
        if sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
        self.__number_of_sim = sim
