from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim
        if self.number_of_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

