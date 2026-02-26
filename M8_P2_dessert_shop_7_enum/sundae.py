from ice_cream import IceCream



class Sundae(IceCream):
    def __init__(
            self,
            name: str = "BaseSundae",
            scoop_count: int = 0,
            price_per_scoop: float = 0.0,
            topping_name: str = "",
            topping_price: float = 0.0
        ):
        super().__init__(name, scoop_count, price_per_scoop)
        self._topping_name: str = topping_name
        self._topping_price: float = topping_price

        self.packaging = "Boat"


    @property
    def topping_name(self) -> str:
        return self._topping_name


    @topping_name.setter
    def topping_name(self, new_topping_name: str):
        if not isinstance(new_topping_name, str):
            raise TypeError(f"Sundae topping name ({new_topping_name}) must be of type string, not ({type(new_topping_name)})!")

        if not new_topping_name:
            raise ValueError("Sundae topping name is required!")
        
        self._topping_name = new_topping_name


    @property
    def topping_price(self) -> float:
        return self._topping_price


    @topping_price.setter
    def topping_price(self, new_topping_price: float):
        if not isinstance(new_topping_price, float) and not isinstance(new_topping_price, int):
            raise TypeError(f"Sundae topping price ({new_topping_price}) must have a numerical type, not {type(new_topping_price)}!")

        if new_topping_price < 0:
            raise ValueError(f"Sundae topping price ({new_topping_price}) cannot be less than 0!")

        self._topping_price = new_topping_price


    def calculate_cost(self) -> float:
        return round(super().calculate_cost() + self._topping_price, 2)
    

    def __repr__(self):
        return f"name: {self.name}, scoop_count: {self.scoop_count}, price_per_scoop: {self.price_per_scoop}, topping_name: {self.topping_name}, topping_price: {self.topping_price}, "
    

    def __str__(self):
        price_str = f"${self.calculate_cost():.2f}"
        tax_str = f"[Tax ${self.calculate_tax():.2f}]"

        detail = f"{self.topping_name} topping @ ${self.topping_price:.2f}:"

        lines = [
            f"{self.topping_name} {self.name} Sundae ({self.packaging})",
            f"{self.scoop_count} scoops of {self.name} ice cream @ ${self.price_per_scoop:.2f}/scoop",
            f"{detail:<47} {price_str:<10} {tax_str}",
        ]

        return "\n     ".join(lines)
