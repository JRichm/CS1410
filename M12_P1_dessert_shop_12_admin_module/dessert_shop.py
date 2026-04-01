from customer import Customer
from order import Order
from candy import Candy
from cookie import Cookie
from icecream import IceCream
from sundae import Sundae
from payable import PayType
from dessert_item import DessertItem



from validators import (
    get_valid_int,
    get_valid_float
)


class DessertShop:
    def __init__(self):
        self.running = True
        self.main()


    def main(self):
        customer_db: dict[str, Customer] = {}

        while self.running:
            print("---Beginning New Order---\n")

            self.order = Order()

            # add default items
            self.seed_order()

            # ask user to add items to the order
            done: bool = False
            while not done:
                try:
                    done = self.user_prompt_item() is None

                except ValueError as e:
                    print(e) 

            customer = self.save_customer_order(self.order, customer_db)


            # ask user to choose a payment type
            payment_method = self.user_prompt_payment()
            self.order.payment_method = payment_method

            # sort the items in the order by price in ascending order
            self.order = self.order.sort()

            # print the order
            print(self.order)
            print(f"-"*76)
            print(f"Customer Name: {customer.customer_name:<23} Customer ID: {customer.customer_id:>6}  Total Orders: {len(customer.order_history)}")


            input("\nPress <Enter> to start a new order.")
            print("\n")


    def save_customer_order(self, order: Order, customer_db: dict[str, Customer]) -> Customer:

        # get customer name from user input
        customer_name = input("\nPlease enter the customer's name: ").strip()

        # add customer to db if user not found
        if customer_name not in customer_db:
            customer_db[customer_name] = Customer(customer_name)

        # get customer from db and add order to history
        customer = customer_db[customer_name]
        customer.add2history(order)

        # return customer
        return customer
    

    def seed_order(self):
        """
            Seed order with the default items
        """
        self.order.add(Candy('Candy Corn', 1.5, 0.25))
        self.order.add(Candy('Gummy Bears', 0.25, 0.35))
        self.order.add(Cookie('Chocolate Chip', 6, 3.99))
        self.order.add(IceCream('Pistachio', 2, 0.79))
        self.order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
        self.order.add(Cookie('Oatmeal Raisin', 2, 3.45))


    def user_prompt_item(self) -> DessertItem:
        """
            Provides User with a menu of items asks for input using children functions
            to handle each item type

        Raises:
            ValueError: Raised when the user enters an invalid input

        Returns:
            DessertItem: The item the user has chosen
        """
        print("\n1: Candy")
        print("2: Cookie")
        print("3: Ice Cream")
        print("4: Sunday")
        choice = input("\nWhat would you like to add to the order? (1-4 or press <Enter> when done): ")

        match choice:
            case "":
                return None
            
            case "1":
                item = self.user_prompt_candy()
            
            case "2":
                item = self.user_prompt_cookie()
            
            case "3":
                item = self.user_prompt_icecream()
            
            case "4":
                item = self.user_prompt_sundae()
            
            case _:
                raise ValueError("Invalid response:  Please enter a choice from the menu (1-4) or press <Enter> when done.")
            
        self.order.add(item)
        print(f"{item.name} has been added to your order.")
        return item


    def user_prompt_candy(self) -> Candy:
        """
            Prompt handler for Candy, asks user for the type, weight, and price per pound.

        Returns:
            Candy: Initialized Candy class populated with user input.
        """
        name: str = input("Enter the type of candy: ")
        weight: float = get_valid_float(
            prompt="Please enter the weight to be purchased: ",
            warning="Error. Candy weight must be a postive number.",
            low=0
        )
        price: float = get_valid_float(
            prompt="Please enter the price per pound: ",
            warning="Error. Price must be a positive number.",
            low=0
        )
        
        return Candy(name, weight, price)


    def user_prompt_cookie(self) -> Cookie:
        """
            Prompt handler for Cookie, asks user for the type, number of cookies, and price per dozen.

        Returns:
            Cookie: Initialized Cookie class populated with user input.
        """
        name: str = input("Enter the type of cookie: ")
        quantity: int = get_valid_int(
            prompt="Please enter the quantity to be purchased: ",
            warning="Error. Number of cookies must be a positive number.",
            low=0
        )
        price: float = get_valid_float(
            prompt="Please enter the price per dozen: ",
            warning="Error. Price per dozen must be a positive number.",
            low=0
        )

        return Cookie(name, quantity, price)


    def user_prompt_icecream(self) -> IceCream:
        """
            Prompt handler for Ice Cream, asks user for the type, number of scoops, and price per scoop.

        Returns:
            IceCream: Initialized IceCream class populated with user input.
        """
        name: str = input("Enter the type of icecream: ")
        num_scoops: int = get_valid_int(
            prompt="Please enter the number of scoops to be purchased: ",
            warning="Error. Number of scoops must be a positive whole number.",
            low=0
        )
        price = float = get_valid_float(
            prompt="Please enter the price per scoop: ",
            warning="Error. Price per scoop must be a positive number.",
            low=0
        )

        return IceCream(name, num_scoops, price)


    def user_prompt_sundae(self) -> Sundae:
        """
            Prompt handler for Sundae, asks u ser for the type, number of scoops, price per scoop, topping type, and price of topping.

        Returns:
            Sundae: Initialized Sundae class populated with user input.
        """
        name: str = input("Enter the type of sundae: ")
        num_scoops: int = get_valid_int(
            prompt="Please enter the number of scoops to be purchased: ",
            warning="Error. Number of scoops must be a positive whole number.",
            low=0
        )
        price = float = get_valid_float(
            prompt="Please enter the price per scoop: ",
            warning="Error. Price per scoop must be a positive number.",
            low=0
        )
        topping_name: str = input("Enter the type of topping: ")
        topping_price: float = get_valid_float(
            prompt="Please enter price of the topping: ",
            warning="Error. Price of topping must be a positive number.",
            low=0
        )

        return Sundae(name, num_scoops, price, topping_name, topping_price)


    def user_prompt_payment(self) -> PayType:
        """
            Prompt handler for Payment Type, asks user for their preferred payment type.

            Validates input by checking to see if user input appears in input map of allowed PayType values

        Returns:
            PayType: Users preferred payment type
        """
        input_map = {
            "1": PayType.CASH,
            "2": PayType.CARD,
            "3": PayType.PHONE,
            "cash": PayType.CASH,
            "card": PayType.CARD,
            "phone": PayType.PHONE,
        }

        while True:
            input_value = input("Enter payment method (Cash, Card, or Phone): ")

            paytype = input_map.get(input_value.lower(), None)
            if paytype:
                return paytype
            
            print("\nInvalid Response: Please enter a valid payment type")



if __name__ == "__main__":
    DessertShop()
    