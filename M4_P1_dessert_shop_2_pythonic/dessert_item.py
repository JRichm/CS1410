class DessertItem:
    def __init__(self, name: str = ""):
        self._name = name


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