from dessert_item import DessertItem



class Cookie(DessertItem):
    def __init__(self, name: str = "BaseCookie", cookie_quantity: int = 0, price_per_dozen: float = 0.0):
        super().__init__(name)
        self._cookie_quantity: int = cookie_quantity
        self._price_per_dozen: float = price_per_dozen


    @property
    def cookie_quantity(self) -> int:
        return self._cookie_quantity


    @cookie_quantity.setter
    def cookie_quantity(self, new_cookie_quantity: int):
        if not isinstance(new_cookie_quantity, int):
            raise TypeError(f"Cookie cookie quantity ({new_cookie_quantity}) must be of type int, not {type(new_cookie_quantity)}")

        if new_cookie_quantity < 0:
            raise ValueError(f"Cookie quantity ({new_cookie_quantity}) cannot be less than 0")
        
        self._cookie_quantity = new_cookie_quantity


    @property
    def price_per_dozen(self) -> float:
        return self._price_per_dozen


    @price_per_dozen.setter
    def price_per_dozen(self, new_price_per_dozen: float):
        if not isinstance(new_price_per_dozen, float) and not isinstance(new_price_per_dozen, int):
            raise TypeError(f"Cookie price per dozen ({new_price_per_dozen}) must be of numerical type, not {type(new_price_per_dozen)}")

        if new_price_per_dozen < 0:
            raise ValueError(f"Cookie price per dozen ({new_price_per_dozen}) cannot be less than 0")
        
        self._price_per_dozen = new_price_per_dozen


    def calculate_cost(self) -> float:
        return round((self._cookie_quantity / 12) * self._price_per_dozen, 2)
    