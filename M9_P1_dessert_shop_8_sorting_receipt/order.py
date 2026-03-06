from dessert_item import DessertItem
from payable import Payable, PayType


class Order(Payable):
    def __init__(self, payment_method: PayType = PayType.CASH):
        self.order: list[DessertItem] = []
        self._payment_method = payment_method

    
    def add(self, item: DessertItem = None):
        if not item or not isinstance(item, DessertItem):
            raise TypeError(f"Invalid item type! (`{str(item)}` {type(item)}) Only items of type <class 'DessertItem'> are allowed.")

        self.order.append(item)


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


    @property
    def payment_method(self) -> PayType:
        return self._payment_method
    

    @payment_method.setter
    def payment_method(self, new_payment_method: PayType):
        if not isinstance(new_payment_method, PayType):
            raise TypeError(f"Payment method must be a valid PayType, not {type(new_payment_method)}")
        
        self._payment_method = new_payment_method


    def sort(self) -> Order:
        # sort the items in the order by price in ascending order
        self.order = sorted(self.order)
        return self


    def __len__(self) -> int:
        return len(self.order)


    def __str__(self):
        lines = ["----------------------------Dessert Shop Receipt----------------------------"]
        lines = lines + [str(o) for o in self.order]

        lines.append("----------------------------------------------------------------------------")
        
        lines.append(f"{'Order Subtotals:':<50} {'$' + str(self.order_cost()):>7} {'$' + str(self.order_tax()):>15}")
        lines.append(f"{'Order Total:':<50} {'$' + str(self.order_cost() + self.order_tax()):>23}")
        lines.append(f"{'Total number of items in order:':<50} {len(self):>23}")
        
        lines.append("----------------------------------------------------------------------------")

        lines.append(f"Paid for with {self.payment_method.name.capitalize()}")

        return "\n".join(lines)