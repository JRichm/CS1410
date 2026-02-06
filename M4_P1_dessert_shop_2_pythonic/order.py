from dessert_item import DessertItem


class Order:
    def __init__(self):
        self.order = []

    
    def add(self, item: DessertItem = None):
        if not item or not isinstance(item, DessertItem):
            raise TypeError(f"Invalid item type! (`{str(item)}` {type(item)}) Only items of type <class 'DessertItem'> are allowed.")

        self.order.append(item)

    
    def __len__(self) -> int:
        return len(self.order)