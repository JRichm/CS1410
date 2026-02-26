from tabulate import tabulate

from order import Order
from candy import Candy
from cookie import Cookie
from ice_cream import IceCream
from sundae import Sundae

from validators import (
    get_valid_int,
    get_valid_float
)


def main():
    order = Order()

    order.add(Candy('Candy Corn', 1.5, 0.25))
    order.add(Candy('Gummy Bears', 0.25, 0.35))
    order.add(Cookie('Chocolate Chip', 6, 3.99))
    order.add(IceCream('Pistachio', 2, 0.79))
    order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    order.add(Cookie('Oatmeal Raisin', 2, 3.45))


    done: bool = False
    while not done:
        print("\n1: Candy")
        print("2: Cookie")
        print("3: Ice Cream")
        print("4: Sunday")
        choice = input("\nWhat would you like to add to the order? (1-4 or press <Enter> when done): ")

        match choice:
            case "":
                done = True
            case "1":
                item = user_prompt_candy()
                order.add(item)
                print(f"{item.name} has been added to your order.")
            case "2":
                item = user_prompt_cookie()
                order.add(item)
                print(f"{item.name} has been added to your order.")
            case "3":
                item = user_prompt_icecream()
                order.add(item)
                print(f"{item.name} has been added to your order.")
            case "4":
                item = user_prompt_sundae()
                order.add(item)
                print(f"{item.name} has been added to your order.")
            case _:
                print("Invalid response:  Please enter a choice from the menu (1-4) or press <Enter> when done.")
    print()

    reciept = [["Name", "Item Cost", "Tax"]]
    for item in order.order:
        item_cost = item.calculate_cost()
        item_tax = item.calculate_tax()
        reciept.append([item.name, f"${item_cost:.2f}", f"${item_tax:.2f}"])

    order_cost = order.order_cost()
    order_tax = order.order_tax()

    dashed_row = ["-"*35, "-"*10, "-"*10]
    reciept.extend(
        [
            dashed_row,
            ["Order Subtotals", f"${order_cost}", f"${order_tax}"],
            ["Order Total", "", f"${order_cost + order_tax:.2f}"],
            ["Total number of items in order", "", len(order)],
            dashed_row
        ]
    )

    print("\n" + tabulate(reciept, headers="firstrow", tablefmt="simple", colalign=("left", "right", "right")) + "\n")
    

def user_prompt_candy() -> Candy:
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


def user_prompt_cookie() -> Cookie:
    name: str = input("Enter the type of cookie: ")
    quantity: int = get_valid_int(
        prompt="Please enter the quantity to be purchased: ",
        warning="Error. Number of cookies must be a positive number.",
        low=0
    )
    price: float = get_valid_int(
        prompt="Please enter the price per dozen: ",
        warning="Error. Price per dozen must be a positive number.",
        low=0
    )

    return Cookie(name, quantity, price)


def user_prompt_icecream() -> IceCream:
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


def user_prompt_sundae() -> Sundae:
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


if __name__ == "__main__":
    main()
    