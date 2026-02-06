from dessert_item import DessertItem



class Candy(DessertItem):
    def __init__(self, name: str = "BaseCandy", candy_weight: float = 0.0, price_per_pound: float = 0.0):
        super().__init__(name)
        self._candy_weight = candy_weight
        self._price_per_pound = price_per_pound


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

    
    def calculate_cost(self):
        return round(self._candy_weight * self._price_per_pound, 2)
    