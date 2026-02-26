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
    

    def __str__(self):
        lines = ["----------------------------Dessert Shop Receipt----------------------------"]
        lines = lines + [str(o) for o in self.order]

        lines.append("----------------------------------------------------------------------------")
        
        lines.append(f"{'Order Subtotals:':<50} {'$' + str(self.order_cost()):>7} {'$' + str(self.order_tax()):>15}")
        lines.append(f"{'Order Total:':<50} {'$' + str(self.order_cost() + self.order_tax()):>23}")
        lines.append(f"{'Total number of items in order:':<50} {len(self):>23}")
        
        lines.append("----------------------------------------------------------------------------")

        return "\n".join(lines)