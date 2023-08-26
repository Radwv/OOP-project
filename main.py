print("welcome to Bascutta Ice Cream")
class IceCreamShop:
    def __init__(self):
        self.menu = []
        self.customer_name = ""

    def ask_customer_name(self):
        self.customer_name = input(" What's your name  ")

    def print_welcome_message(self):
        print("Welcome", self.customer_name + "!")

    def print_menu(self):
        print("Ice Cream Menu:")
        for item in self.menu:
            print(item)

    def place_order(self):
        self.ask_customer_name()
        self.print_welcome_message()

        start_order = input("Do you want to start making an order? (Yes , No) ")
        if start_order.lower() == "yes":
            self.print_menu()
            order = []
            while True:
                choice = input("Choose the type of ice cream you would like(Or type 'done' to finished) ")
                if choice == "done":
                    break
                order.append(choice)

                add_more = input("Do you want to add something else?(Yes , No)  ")
                if add_more.lower() == "yes":
                    self.print_menu()
                else:
                    break

            payment_method = input("Would you like the payment method to be cash or visa? ")
            print("Your request has been registered successfully.")
            print("Your order:", order)
            print("payment method:", payment_method)
            print("Thank you, we are pleased to deal with you.", self.customer_name + "!")

        else:
            print("Thank you for your visit", self.customer_name + "!")

#code
shop = IceCreamShop()
shop.menu = ["Vanilla","Chocolate","Strawberry","Mint Chocolate Chip","Cookies and Cream","Rocky Road","Butter Pecan","Coffee","Salted Caramel","Cookie Dough"]

shop.place_order()
