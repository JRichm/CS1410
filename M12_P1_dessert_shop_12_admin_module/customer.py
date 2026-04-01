from order import Order

class Customer:
    _next_id: int = 1000

    def __init__(self, customer_name: str = "BaseCustomer"):
        self._customer_id: int = Customer._next_id
        self._customer_name: str = customer_name
        self._order_history: list[Order] = []

        Customer._next_id += 1


    @property
    def customer_id(self) -> int:
        return self._customer_id

        
    @property
    def customer_name(self) -> str:
        return self._customer_name
    

    @customer_name.setter
    def customer_name(self, new_customer_name: str):
        self._customer_name = new_customer_name

        
    @property
    def order_history(self) -> list[Order]:
        return self._order_history

    
    def add2history(self, order: Order) -> Customer:
        self._order_history.append(order)