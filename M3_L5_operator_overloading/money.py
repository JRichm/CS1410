"""
Author: James Richmond
Date: 01/19/2026
"""


class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
        self.normalize()


    def normalize(self):
        if self.cents >= 100:
            self.dollars += self.cents // 100
            self.cents = self.cents % 100

        # handle negative cents
        elif self.cents < 0:
            neg_dollars = (99 - self.cents) // 100
            self.dollars -= neg_dollars
            self.cents += neg_dollars * 100


    # addition overload
    def __add__(self, other):
        print(f"adding {self} and {other}")
        
        cents = self.cents + other.cents
        dollars = self.dollars + other.dollars
        return Money(dollars, cents)
    

    # subtraction overload (bonus)
    def __sub__(self, other):
        print(f"subtracting {other} from {self}")

        cents = self.cents - other.cents
        dollars = self.dollars - other.dollars
        return Money(dollars, cents)


    # multiplication overload
    def __mul__(self, scalar: int):
        print(f"multiplying {self} and {scalar}")
        cents = self.cents * scalar
        dollars = self.dollars * scalar
        return Money(dollars, cents)


    # reverse multiplication overload
    def __rmul__(self, scalar):
        return self.__mul__(scalar)


    # equality overload
    def __eq__(self, other):
        print(f"checking equality between {self} and {other}")

        return self.dollars == other.dollars and self.cents == other.cents


    def __str__(self):
        return f"${self.dollars}.{self.cents:02d}"



def main():

    # initialize and print starting values
    print(f"starting values:")
    m1 = Money(3, 50)
    m2 = Money(2, 75)
    print("   m1:", m1)
    print("   m2:", m2, "\n")

    # Part 1 - addition
    m3 = m1 + m2
    print("   result (m3):", m3, "\n")

    # Part 2 - multiplication
    m4 = m1 * 2
    print("   result (m4):", m4, "\n")

    # Part 2 - reverse multiplication
    m5 = 3 * m2
    print("   result (m5):", m5, "\n")

    # Bonus - subtraction
    m6 = m2 - m1
    print("   result (mB):", m6, "\n")

    # Part 3 - equality
    eq = m1 == m2
    print("   result (eq):", eq, "\n")
    print("   ", m1 == Money(2, 150), "\n")  # Expected: True
    print("   ", m1 == Money(3, 49))   # Expected: False



if __name__ == "__main__":
    main()