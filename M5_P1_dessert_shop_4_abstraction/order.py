from dessert_item import DessertItem


class Order:
    def __init__(self):
        self.order: list[DessertItem] = []

    
    def add(self, item: DessertItem = None):
        if not item or not isinstance(item, DessertItem):
            raise TypeError(f"Invalid item type! (`{str(item)}` {type(item)}) Only items of type <class 'DessertItem'> are allowed.")

        self.order.append(item)

    
    def __len__(self) -> int:
        return len(self.order)


    def order_cost(self) -> float:
        cost_items = 0
        for item in self.order:
            cost_items += item.calculate_cost()

        return round(cost_items, 2)


    def order_tax(self) -> float:
        cost_tax = 0
        for item in self.order:
            cost_tax += item.calculate_tax()
            
        return round(cost_tax, 2)
    