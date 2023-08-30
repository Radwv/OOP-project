import tkinter as tk
from tkinter import simpledialog

class IceCreamShop:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ice Cream Shop")
        self.customer_name = ""
        self.menu = []
        self.prices = {}

    def run(self):
        self.get_customer_name()
        self.print_welcome_message()
        self.print_menu()
        self.place_order()
        self.root.mainloop()

    def get_customer_name(self):
        self.customer_name = simpledialog.askstring("Customer Name", "Enter your name:")

    def print_welcome_message(self):
        welcome_label = tk.Label(self.root, text="Welcome " + self.customer_name + "!")
        welcome_label.pack()

    def print_menu(self):
        menu_frame = tk.Frame(self.root)
        menu_frame.pack()

        menu_label = tk.Label(menu_frame, text="Ice Cream Menu:")
        menu_label.pack()

        self.menu_listbox = tk.Listbox(menu_frame)
        self.menu_listbox.pack()

        for item in self.menu:
            self.menu_listbox.insert(tk.END, item)

    def place_order(self):
        order_frame = tk.Frame(self.root)
        order_frame.pack()

        order_label = tk.Label(order_frame, text="Your order:")
        order_label.pack()

        self.order_listbox = tk.Listbox(order_frame)
        self.order_listbox.pack()

        self.total_cost = 0

        self.entry_ice_cream = tk.Entry(self.root)
        self.entry_ice_cream.pack()

        self.button_add = tk.Button(self.root, text="Add", command=self.add_ice_cream)
        self.button_add.pack()

        self.button_finish = tk.Button(self.root, text="Finish", command=self.finish_order)
        self.button_finish.pack()

    def add_ice_cream(self):
        choice = self.entry_ice_cream.get()
        if choice == "done":
            self.finish_order()
        elif choice in self.menu:
            self.order_listbox.insert(tk.END, choice)
            self.total_cost += self.prices[choice]
            self.entry_ice_cream.delete(0, tk.END)

    def finish_order(self):
        payment_method = simpledialog.askstring("Payment Method", "Enter payment method:")
        order_summary = "Customer Name: " + self.customer_name + "\n"
        order_summary += "Order Items: " + ", ".join(self.order_listbox.get(0, tk.END)) + "\n"
        order_summary += "Total Cost: $" + str(self.total_cost) + "\n"
        order_summary += "Payment Method: " + payment_method

        self.label_order_summary = tk.Label(self.root, text=order_summary)
        self.label_order_summary.pack()

if __name__ == "__main__":
    shop = IceCreamShop()
    shop.menu = ["Vanilla","Chocolate","Strawberry","Mint Chocolate Chip","Cookies and Cream","Rocky Road","Butter Pecan","Coffee","Salted Caramel","Cookie Dough"]
    shop.prices = {"Vanilla": 20, "Chocolate": 25, "Strawberry": 25, "Mint Chocolate Chip": 35, "Cookies and Cream": 35, "Rocky Road": 30, "Butter Pecan": 30, "Coffee": 25, "Salted Caramel": 30, "Cookie Dough": 35}
    shop.run()
