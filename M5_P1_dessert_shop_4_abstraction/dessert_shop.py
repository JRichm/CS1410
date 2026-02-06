from tabulate import tabulate

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
    

if __name__ == "__main__":
    main()
    