
class InstantiateCSVError(Exception):
    def __init__(self):
        self.message = 'Файл item.csv поврежден'
