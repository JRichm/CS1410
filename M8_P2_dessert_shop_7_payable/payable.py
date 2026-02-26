from typing import Protocol
from enum import Enum

class PayType(Enum):
    CASH = 1
    CARD = 2
    PHONE = 3


class Payable(Protocol):
    def __init__(self):
        self._payment_method: PayType

    
    @property
    def payment_method(self) -> PayType:
        return self._payment_method
    

    @payment_method.setter
    def payment_method(self, new_payment_method: PayType):
        self._payment_method = new_payment_method
