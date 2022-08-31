from classes.storage import Storage


class Store(Storage):
    def __init__(self):
        self._items = {}
        self._capacity = 100

    def add(self, title, count):
        if title in self._items:
            self._items[title] += count
        else:
            self._items[title] = count
        self._capacity -= count

    def remove(self, title, count):
        res = self._items[title] - count
        if res > 0:
            self._items[title] = res
        else:
            del self._items[title]
        self._capacity += count

    @property
    def get_free_space(self):
        return self._capacity

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, new_items):
        self._items = new_items
        self._capacity -= sum(self._items.values())

    @property
    def get_unique_items_count(self):
        return len(self._items.keys())
