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

BANNER_WIDTH = 75
MENU_WIDTH = 30



class DessertShop:
    def __init__(self):
        self.running = True
        self.main()


    def main(self):
        customer_db: dict[str, Customer] = {}
        # customer_db = self.seed_customer_db(customer_db)

        while self.running:
            print("---Beginning New Order---")

            self.order = Order()

            # add default items
            self.order = self.seed_order(self.order)

            # ask user to add items to the order
            done: bool = False
            while not done:
                try:
                    done = self.user_prompt_item(customer_db) is None

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
        customer_name = None
        while not customer_name:
            customer_name = input("\nPlease enter the customer's name: ").strip()

        # add customer to db if user not found
        if customer_name not in customer_db:
            customer_db[customer_name] = Customer(customer_name)

        # get customer from db and add order to history
        customer = customer_db[customer_name]
        customer.add_to_history(order)

        # return customer
        return customer
    

    def seed_order(self, order):
        """
            Seed order with the default items
        """
        order.add(Candy('Gummy Bears', 0.25, 0.35))
        order.add(Candy('Candy Corn', 1.5, 0.25))
        order.add(Cookie('Oatmeal Raisin', 2, 3.45))
        order.add(IceCream('Pistachio', 2, 0.79))
        order.add(Cookie('Chocolate Chip', 6, 3.99))
        order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))

        return order


    def seed_customer_db(self, customer_db: dict):
        # James
        james = Customer("James")
        james_order = Order(PayType.CARD)
        james_order = self.seed_order(james_order)

        for item in [
            Candy("Brocks", .01, .1),
            Candy("Molasses Gum", 0.1, .1),
            Cookie("Chocolate Chip", 1, 12),
            Cookie("Snickerdoodles", 1, 9),
            Cookie("Sugar", 1, 6),
            IceCream("Strawberry", 1, .5),
            IceCream("Vanilla", 1, .3),
        ]:
            james_order.add(item)

        james.add_to_history(james_order)

        # Karis
        karis = Customer("Karis")

        for x in range(4):
            karis_order = Order(PayType.CARD)
            karis_order = self.seed_order(karis_order)
            karis.add_to_history(karis_order)

        # Mei
        mei = Customer("Mei")
        mei_order = Order(PayType.PHONE)
        mei_order = self.seed_order(mei_order)

        for item in [
            Candy("Snickers", 5, 9.85),
            Candy("Reces", 5, 9.85),
            Cookie("Chocolate Chip", 36, 12),
            Cookie("White Chocolate Macadamia", 36, 18),
        ]:
            mei_order.add(item)

        mei.add_to_history(mei_order)

        for customer in [james, karis, mei]:
            customer_db[customer.customer_name] = customer

        return customer_db


    def user_prompt_item(self, customer_db) -> DessertItem:
        """
            Provides User with a menu of items asks for input using children functions
            to handle each item type

        Raises:
            ValueError: Raised when the user enters an invalid input

        Returns:
            DessertItem: The item the user has chosen
        """
        self.print_header("Main Menu", width = MENU_WIDTH)
        print("1: Candy")
        print("2: Cookie")
        print("3: Ice Cream")
        print("4: Sunday")
        print("5: Admin Module")
        choice = input("\nWhat would you like to add to the order? (1-4, <5> for Admin, <Enter> for done): ")


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
            
            case "5":
                self.admin_menu(customer_db)
                return True

            case _:
                raise ValueError("Invalid response:  Please enter a choice from the menu (1-5) or Enter")
            
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
        price: float = get_valid_float(
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
        price: float = get_valid_float(
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


    def admin_menu(self, customer_db: dict):
        options = [
            "Shop's Customer List",
            "Customer Order History",
            "Most Frequent Customer",
            "Best Customer",
            "Customer With Largest Order"
        ]

        admin = True
        while admin:
            print("\n")
            self.print_header("Admin Menu", width=MENU_WIDTH)
            for x, option in enumerate(options):
                print(f"{x+1}: {option}")

            choice = input(f"What would you like to do? (1-{len(options)}, <Enter> to return to the previous menu): ")

            match choice:
                case "1":
                    self.store_customer_list(customer_db)
                case "2":
                    self.customer_order_history(customer_db)
                case "3":
                    self.most_frequent_customer(customer_db)
                case "4":
                    self.best_customer(customer_db)
                case "5":
                    self.biggest_order(customer_db)
                case "":
                    print("\n")
                    return
                case _:
                    print("Invalid response:  Please enter a choice from the menu (1-5) or Enter")

    
    def print_header(self, message: str, sub_message: tuple = (), width: int = MENU_WIDTH):
        width = width + 1
        w = width - 4

        # print("\n\n")
        print("*"*width)
        print(f"**{message:^{w}}**")
        if sub_message:
            print(f"**   {sub_message[0]}{sub_message[1]:>{width-len(sub_message[0]) - 10}}   **")
        print("*"*width)


    def store_customer_list(self, customer_db: dict[str,Customer]) -> None:
        '''
        Displays a list of all Dessert Shop customers and their Customer IDs in a nice format, as shown in the Example Run.
        This function should NOT use the dictionary key to parse through each customer in the customer_db dictionary
        (Refer to your reading and video assignments).
        '''

        print("\n\n")
        self.print_header(message="Dessert Shop Customer List", width=BANNER_WIDTH)
        if len(customer_db) == 0:
            print(f"No customers yet.")
            return

        for customer in customer_db.values():
            row = (f"Customer Name: {customer.customer_name}", f"Customer ID: {customer.customer_id}")
            print(f"{row[0]} {row[1]:>{BANNER_WIDTH-len(row[0])}}")


    def customer_order_history(self, customer_db: dict[str,Customer]) -> None:
        '''
        Prompts the user for a customer name and then prints all orders (receipts) for that customer, labeling each
        receipt with a sequential order number, as shown in the Example Run. If the user enters a name that is not in
        the customer_db dictionary, provide an error message as shown in the Example Run. This function should use
        enumerate to retrieve both the order details and generate an order number.
        '''

        print("\n\n")
        self.print_header(message="Customer Order History", width=BANNER_WIDTH)
        if len(customer_db) == 0:
            print("No customers yet")
            return


        customer_name = input("Please enter the customer's name: ")

        customer = customer_db.get(customer_name, None)
        if customer is None:
            print(f"Error. The Dessert Shop customer list does not contain a customer named '{customer_name}'.\nCheck both spelling and capitalizaiton of your entry.")
            return False
        

        print("\n\n")
        self.print_header(message="Order History For:", sub_message=(f"Customer Name: {customer_name}", f"Customer ID: {customer.customer_id}"), width=BANNER_WIDTH)

        for order_number, order in enumerate(customer.order_history):
            print(f"\n\nOrder # {order_number + 1}")
            print(order)


    def most_frequent_customer(self, customer_db: dict[str,Customer]) -> None:
        '''
        Displays a banner showing the Most Frequent Customer AND the number of orders they have made, based on the
        number of orders each customer has made, as shown in the Example Run. Do NOT use a for loop in this function.
        This function requires you to find two values using the following Pythonic and/or object-oriented approaches:
        This function should use the max() function, with the key defined by a lambda function that returns the size of
        each customer's order history. Once you have found the Most Frequent Customer, finding the number of orders
        that customer has made is trivial using OOP.
        '''
        if len(customer_db) == 0:
            self.print_header(message="Most Frequent Customer", width=BANNER_WIDTH)
            print("No customers yet")
            return

        name, customer = max(customer_db.items(), key=lambda item: len(item[1].order_history))
        
        print("\n\n")
        self.print_header(message=f"{customer.customer_name} is the most frequent customer with {len(customer.order_history)} order(s)!", width=BANNER_WIDTH)


    def best_customer(self, customer_db: dict[str,Customer]) -> None:
        '''
        Displays a banner showing the Best Customer AND the total amount of money they have spent, based on each customer's
        total spend at the shop, as shown in the Example Run. Do NOT use a for loop in this function. This function
        requires you to find two values using the following Pythonic and/or object-oriented approaches:
            To find the Best Customer, this function should:
                Use the max() function
                Have a key in the max() function defined by a lambda function
                Have a lambda function where the body of the lambda is the sum() of an iterable of order costs
                Use the sum() function with an iterable of order costs generated by a list comprehension
                Find the Best Customer in a single written line of code using the formula outlined here.
            To find the total spent by the Best Customer, this function should:
                Use the sum() function with an iterable of order costs generated by a list comprehension
                Calculate the total spent in a single written line of code using the formula outlined here.
        '''
        if len(customer_db) == 0:
            self.print_header(message="The Best Customer", width=BANNER_WIDTH)
            print("No customers yet")
            return

        name, customer = max(customer_db.items(), key=lambda item: sum([o.order_cost() for o in item[1].order_history]))
        customer_total = sum([o.order_cost() for o in customer.order_history])
    
        print("\n\n")
        self.print_header(message=f"{customer.customer_name} is the best customer having spent ${customer_total:.2f} at the Dessert Shop!", width=BANNER_WIDTH)


    def biggest_order(self, customer_db: dict[str,Customer]) -> None:
        '''
        Displays a banner showing the customer who made the order with the most items in it AND the total number of items
        in that order, as shown in the Example Run. You may use any approach you want to write this function (except for
        hard-coding the printout to contain the right answer). Expect that the test for grading will not match the Example
        Run to prevent hard-coded answers from being accepted. (Plus, the instructor personally reviews all code)
        '''
        if len(customer_db) == 0:
            self.print_header(message="The Largest Order", width=BANNER_WIDTH)
            print("No customers yet")
            return

        name, customer = max(customer_db.items(), key=lambda item: max([len(o) for o in item[1].order_history]))
        largest_order = max(customer.order_history, key=lambda o: len(o))

        print("\n\n")
        self.print_header(message=f"{customer.customer_name} made the largest order with a whopping {len(largest_order)} items!", width=BANNER_WIDTH)



if __name__ == "__main__":
    DessertShop()
    