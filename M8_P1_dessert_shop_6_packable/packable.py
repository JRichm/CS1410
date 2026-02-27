class Packable:
    def __init__(self, packaging: str):
        self._packaging = packaging

    
    @property
    def packaging(self) -> str:
        return self._packaging
    

    @packaging.setter
    def packaging(self, new_packaging: str):
        self._packaging = new_packaging