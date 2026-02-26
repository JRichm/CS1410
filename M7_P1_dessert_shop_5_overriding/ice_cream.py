from dessert_item import DessertItem



class IceCream(DessertItem):
    def __init__(self, name: str = "BaseIceCream", scoop_count: int = 0, price_per_scoop: float = 0.0):
        super().__init__(name)
        self._scoop_count: int = scoop_count
        self._price_per_scoop: float = price_per_scoop
    

    @property
    def scoop_count(self) -> int:
        return self._scoop_count

    
    @scoop_count.setter
    def scoop_count(self, new_scoop_count: int):
        if not isinstance(new_scoop_count, int):
            raise TypeError(f"Ice Cream new scoop count ({new_scoop_count}) must be of type int, not {type(new_scoop_count)}")

        if new_scoop_count < 0:
            raise ValueError(f"Ice Cream scoop count ({new_scoop_count}) cannot be less than 0!")

        self._scoop_count = new_scoop_count


    @property
    def price_per_scoop(self) -> float:
        return self._price_per_scoop

    
    @price_per_scoop.setter
    def price_per_scoop(self, new_price_per_scoop: float):
        if not isinstance(new_price_per_scoop, float) and not isinstance(new_price_per_scoop, int):
            raise TypeError(f"Ice Cream price per scoop ({new_price_per_scoop}) must be numerical, not {type(new_price_per_scoop)}")
        
        if new_price_per_scoop < 0:
            raise ValueError(f"Ice Cream price per scoop {new_price_per_scoop} cannot be less than 0!")

        self._price_per_scoop = new_price_per_scoop


    def calculate_cost(self) -> float:
        return round(self._scoop_count * self._price_per_scoop, 2)
    

    def __repr__(self):
        return f"name: {self.name}, scoop_count: {self.scoop_count}, price_per_scoop: {self.price_per_scoop}"
    

    def __str__(self):
        price_str = f"${self.calculate_cost():.2f}"
        tax_str = f"[Tax ${self.calculate_tax():.2f}]"

        detail = f"{self.scoop_count} scoops @ ${self.price_per_scoop:.2f}/scoop:"

        lines = [
            f"{self.name} Ice Cream",
            f"{detail:<47} {price_str:<10} {tax_str}"
        ]

        return "\n     ".join(lines)

