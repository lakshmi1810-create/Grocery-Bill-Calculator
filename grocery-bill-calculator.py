from datetime import datetime
import random


class GroceryBillCalculator:

    GST_RATE = 0.05
    DISCOUNT_RATE = 0.25
    DISCOUNT_LIMIT = 2000

    def __init__(self):
        self.customer_name = ""
        self.bill_no = random.randint(1000, 9999)
        self.date = datetime.now()
        self.items = []
        self.subtotal = 0
        self.gst = 0
        self.discount = 0
        self.final_bill = 0

    def customer_details(self):
        print("\n========== CUSTOMER DETAILS ==========")
        self.customer_name = input("Customer Name : ")

    def add_items(self):
        while True:
            item_name = input("\nItem Name : ")

            try:
                price = float(input("Price : ₹"))
                if price <= 0:
                    raise ValueError

                quantity = int(input("Quantity : "))
                if quantity <= 0:
                    raise ValueError

            except ValueError:
                print("Invalid Input! Please enter valid values.")
                continue

            total = price * quantity

            self.items.append({
                "name": item_name,
                "price": price,
                "quantity": quantity,
                "total": total
            })

            print("Item Added Successfully!")

            choice = input("\nAdd another item? (Y/N): ").lower()
            if choice != "y":
                break

    def display_cart(self):
        if len(self.items) == 0:
            print("\nCart is Empty.")
            return

        print("\n================ CART ================")

        for item in self.items:
            print(
                f"{item['name']:15} "
                f"₹{item['price']:8.2f} "
                f"x {item['quantity']:2} "
                f"= ₹{item['total']:.2f}"
            )

    def search_item(self):
        name = input("\nEnter item to search : ").lower()

        for item in self.items:
            if item["name"].lower() == name:
                print("\nItem Found")
                print(item)
                return

        print("Item not found.")

    def remove_item(self):
        name = input("\nEnter item to remove : ").lower()

        for item in self.items:
            if item["name"].lower() == name:
                self.items.remove(item)
                print("Item Removed Successfully.")
                return

        print("Item not found.")

    def calculate_bill(self):
        self.subtotal = sum(item["total"] for item in self.items)
        self.gst = self.subtotal * self.GST_RATE

        if self.subtotal >= self.DISCOUNT_LIMIT:
            self.discount = self.subtotal * self.DISCOUNT_RATE

        self.final_bill = self.subtotal + self.gst - self.discount

    def payment_method(self):
        print("\nChoose Payment Method")
        print("1. Cash")
        print("2. UPI")
        print("3. Credit Card")
        print("4. Debit Card")

        choice = input("Choice : ")

        methods = {
            "1": "Cash",
            "2": "UPI",
            "3": "Credit Card",
            "4": "Debit Card"
        }

        return methods.get(choice, "Cash")

    def print_receipt(self):
        payment = self.payment_method()
        self.calculate_bill()

        print("\n")
        print("=" * 45)
        print("          GROCERY STORE")
        print("=" * 45)

        print("Bill No :", self.bill_no)
        print("Date    :", self.date.strftime("%d-%m-%Y %H:%M"))
        print("Customer:", self.customer_name)

        print("-" * 45)

        for item in self.items:
            print(
                f"{item['name']:15}"
                f"{item['quantity']} x ₹{item['price']:.2f}"
                f" = ₹{item['total']:.2f}"
            )

        print("-" * 45)

        print(f"Subtotal : ₹{self.subtotal:.2f}")
        print(f"GST (5%) : ₹{self.gst:.2f}")
        print(f"Discount : ₹{self.discount:.2f}")

        print("-" * 45)

        print(f"Final Bill : ₹{self.final_bill:.2f}")
        print("Payment    :", payment)

        print("=" * 45)

        self.save_receipt(payment)

    def save_receipt(self, payment):
        filename = f"Bill_{self.bill_no}.txt"

        with open(filename, "w") as file:
            file.write("GROCERY STORE\n")
            file.write(f"Bill No : {self.bill_no}\n")
            file.write(f"Customer : {self.customer_name}\n")
            file.write(f"Date : {self.date}\n\n")

            for item in self.items:
                file.write(
                    f"{item['name']} "
                    f"{item['quantity']} x "
                    f"{item['price']} = "
                    f"{item['total']}\n"
                )

            file.write("\n")
            file.write(f"Subtotal : {self.subtotal}\n")
            file.write(f"GST : {self.gst}\n")
            file.write(f"Discount : {self.discount}\n")
            file.write(f"Final Bill : {self.final_bill}\n")
            file.write(f"Payment : {payment}\n")


def main():
    grocery = GroceryBillCalculator()
    grocery.customer_details()

    while True:
        print("\n========== MENU ==========")
        print("1. Add Items")
        print("2. View Cart")
        print("3. Search Item")
        print("4. Remove Item")
        print("5. Generate Bill")
        print("6. Exit")

        choice = input("Enter Choice : ")

        if choice == "1":
            grocery.add_items()
        elif choice == "2":
            grocery.display_cart()
        elif choice == "3":
            grocery.search_item()
        elif choice == "4":
            grocery.remove_item()
        elif choice == "5":
            grocery.print_receipt()
        elif choice == "6":
            print("\nThank You for Visiting!")
            break
        else:
            print("Invalid Choice.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram Interrupted.")
    except Exception as e:
        print("Unexpected Error :", e)