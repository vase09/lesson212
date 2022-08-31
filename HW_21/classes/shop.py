from classes.store import Store


class Shop(Store):
    def __init__(self):
        super().__init__()
        self._capacity = 20
