from typing import Protocol
from enum import Enum


class PayType(Enum):
    CASH = 1
    CARD = 2
    PHONE = 3


class Payable(Protocol):
    
    @property
    def payment_method(self) -> PayType:
        ...
    

    @payment_method.setter
    def payment_method(self, new_payment_method: PayType):
        ...