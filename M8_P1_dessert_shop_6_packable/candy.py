from dessert_item import DessertItem



class Candy(DessertItem):
    def __init__(self, name: str = "BaseCandy", candy_weight: float = 0.0, price_per_pound: float = 0.0):
        super().__init__(name)
        self._candy_weight: float = candy_weight
        self._price_per_pound: float = price_per_pound

        self.packaging = "Bag"


    @property
    def candy_weight(self) -> float:
        return self._candy_weight


    @candy_weight.setter
    def candy_weight(self, new_weight: float):
        if not isinstance(new_weight, float) and not isinstance(new_weight, int):
            raise TypeError(f"Candy weight ({new_weight}) must be of numerical type, not {type(new_weight)}")

        if new_weight < 0:
            raise ValueError(f"Candy weight ({new_weight}) cannot be less than 0!")

        self._candy_weight = new_weight


    @property
    def price_per_pound(self) -> float:
        return self._price_per_pound


    @price_per_pound.setter
    def price_per_pound(self, new_price_per_pound: float):
        if not isinstance(new_price_per_pound, float) and not isinstance(new_price_per_pound, int):
            raise TypeError(f"Candy price per pound ({new_price_per_pound}) must be of numerical type, not {type(new_price_per_pound)}")

        if new_price_per_pound < 0:
            raise ValueError(f"Candy price per pound ({new_price_per_pound}) cannot be less than 0!")

        self._price_per_pound = new_price_per_pound

    
    def calculate_cost(self) -> float:
        return round(self._candy_weight * self._price_per_pound, 2)
    

    def __repr__(self):
        return f"name: {self.name}, candy_weight: {self.candy_weight}, price_per_pound: {self.price_per_pound}"


    def __str__(self):
        price_str = f"${self.calculate_cost():.2f}"
        tax_str = f"[Tax ${self.calculate_tax():.2f}]"

        detail = f"{self.candy_weight} lbs. @ ${self.price_per_pound}/lb.:"

        lines = [
            f"{self.name} Candy ({self.packaging})",
            f"{detail:<47} {price_str:<10} {tax_str}"
        ]

        return  "\n     ".join(lines)
