from abc import ABC, abstractmethod

class DessertItem(ABC):
    def __init__(self, name: str = "", tax_percent: float = 7.25):
        self._name: str = name
        self._tax_percent: float = tax_percent
        self._packaging = None


    @property
    def name(self) -> str:
        return self._name
    

    @name.setter
    def name(self, new_name: str = ""):
        if not isinstance(new_name, str):
            raise TypeError(f"`{new_name}` is not valid name for {self.__class__.__name__}")
        
        if not new_name:
            raise ValueError(f"Unable to set name of {self.__class__.__name__} to an empty string")
        
        self._name = new_name


    @property
    def tax_percent(self) -> float:
        return self._tax_percent


    @tax_percent.setter
    def tax_percent(self, new_tax_percent: float):
        self._tax_percent = new_tax_percent


    @abstractmethod
    def calculate_cost(self) -> float:
        pass


    def calculate_tax(self) -> float:
        return round(self.calculate_cost() * self._tax_percent * 0.01, 2)


    @property
    def packaging(self) -> str:
        return self._packaging
    

    @packaging.setter
    def packaging(self, new_packaging: str):
        self._packaging = new_packaging
