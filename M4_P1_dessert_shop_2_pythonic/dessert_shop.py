from order import Order
from candy import Candy
from cookie import Cookie
from ice_cream import IceCream
from sundae import Sundae



def main():
    order = Order()

    for item in [
        Candy("Candy Corn", 1.5, .25),
        Candy("Gummy Bears", .25, .35),
        Cookie("Chocolate Chip", 6, 3.99),
        IceCream("Pistachio", 2, .79),
        Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29),
        Cookie("Oatmeal Raisin", 2, 3.45),
    ]:
        order.add(item)

    for item in order.order:
        print(item.name)    

    print(f"Total number of items in order: {len(order)}")


if __name__ == "__main__":
    main()