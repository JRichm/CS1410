from typing import Protocol


class Packable:

    @property
    def packaging(self) -> str:
        ...
    

    @packaging.setter
    def packaging(self, new_packaging: str):
        ...
