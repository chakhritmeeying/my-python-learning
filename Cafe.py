class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class Cafe:
    def __init__(self):
        self.order = []

    def add_order(self, coffee):
        self.order.append(coffee)
        print(f"Added {coffee.name} to your order.")

    def display_order(self):
        if not self.order:
            print("Your order is empty.")
            return
        print("Your order:")
        for coffee in self.order:
            print(coffee)

    def calculate_total(self):
        return sum(coffee.price for coffee in self.order)

    def checkout(self):
        if not self.order:
            print("Your order is empty.")
            return
        total = self.calculate_total()
        print(f"Your total is : ${total:.2f}")
        print("Thank you.")
        self.order.clear()


def main():

    menu = [
        Coffee("Espresso", 2.50),
        Coffee("Latte", 3.50),
        Coffee("Cappuccino", 2.50),
        Coffee("Americano", 2.00),
        Coffee("Mocha", 3.00)
    ]

    order = Cafe()
    while True:
        print("\n----- Coffee Menu -----")
        for idx, coffee in enumerate(menu, 1):
            print(f"{idx}. {coffee.name} - ${coffee.price:.2f}")

        print("01. View Order")
        print("02. Checkout")
        print("00. Exit")
        choice = input("Choose an option: ")
        if choice in [str(idx) for idx in range(1, len(menu)+1)]:
            order.add_order(menu[int(choice)-1])
        elif choice == "01":
            order.display_order()
        elif choice == "02":
            order.checkout()
        elif choice == "00":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
