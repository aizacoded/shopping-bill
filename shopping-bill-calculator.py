import tkinter as tk
from tkinter import messagebox


class ShoppingBill:

    def __init__(self, root):
        self.root = root
        self.root.title("Shopping Bill")
        self.root.geometry("430x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#eeeeee")

        self.cart = []

        self.create_ui()

    # ---------------- UI ----------------

    def create_ui(self):

        # Header
        header = tk.Frame(
            self.root,
            bg="#202020",
            height=75
        )
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="SHOPPING BILL",
            font=("Arial", 21, "bold"),
            fg="white",
            bg="#202020"
        ).pack(pady=(15, 0))

        tk.Label(
            header,
            text="Add items to your cart",
            font=("Arial", 9),
            fg="#aaaaaa",
            bg="#202020"
        ).pack()

        # Input area
        input_frame = tk.Frame(
            self.root,
            bg="#eeeeee"
        )
        input_frame.pack(
            fill="x",
            padx=25,
            pady=20
        )

        tk.Label(
            input_frame,
            text="ITEM NAME",
            font=("Arial", 8, "bold"),
            bg="#eeeeee",
            fg="#555555"
        ).pack(anchor="w")

        self.item_entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            relief="flat",
            bg="white"
        )
        self.item_entry.pack(
            fill="x",
            ipady=9,
            pady=(3, 10)
        )

        # Price and quantity
        row = tk.Frame(
            input_frame,
            bg="#eeeeee"
        )
        row.pack(fill="x")

        price_frame = tk.Frame(
            row,
            bg="#eeeeee"
        )
        price_frame.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 8)
        )

        tk.Label(
            price_frame,
            text="PRICE (₹)",
            font=("Arial", 8, "bold"),
            bg="#eeeeee",
            fg="#555555"
        ).pack(anchor="w")

        self.price_entry = tk.Entry(
            price_frame,
            font=("Arial", 12),
            relief="flat",
            bg="white"
        )
        self.price_entry.pack(
            fill="x",
            ipady=9,
            pady=3
        )

        quantity_frame = tk.Frame(
            row,
            bg="#eeeeee"
        )
        quantity_frame.pack(
            side="right",
            fill="x",
            expand=True,
            padx=(8, 0)
        )

        tk.Label(
            quantity_frame,
            text="QUANTITY",
            font=("Arial", 8, "bold"),
            bg="#eeeeee",
            fg="#555555"
        ).pack(anchor="w")

        self.quantity_entry = tk.Entry(
            quantity_frame,
            font=("Arial", 12),
            relief="flat",
            bg="white"
        )
        self.quantity_entry.pack(
            fill="x",
            ipady=9,
            pady=3
        )

        # Add button
        tk.Button(
            input_frame,
            text="+  ADD TO CART",
            font=("Arial", 10, "bold"),
            bg="#202020",
            fg="white",
            activebackground="#444444",
            activeforeground="white",
            relief="flat",
            command=self.add_item
        ).pack(
            fill="x",
            pady=(15, 0),
            ipady=10
        )

        # Cart heading
        tk.Label(
            self.root,
            text="YOUR CART",
            font=("Arial", 9, "bold"),
            bg="#eeeeee",
            fg="#555555"
        ).pack(
            anchor="w",
            padx=25
        )

        # Cart display
        self.cart_frame = tk.Frame(
            self.root,
            bg="white"
        )
        self.cart_frame.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=(5, 15)
        )

        # Bottom buttons
        bottom = tk.Frame(
            self.root,
            bg="#eeeeee"
        )
        bottom.pack(
            fill="x",
            padx=25,
            pady=(0, 20)
        )

        tk.Button(
            bottom,
            text="CLEAR CART",
            font=("Arial", 9, "bold"),
            bg="#dddddd",
            fg="#202020",
            relief="flat",
            command=self.clear_cart
        ).pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 5),
            ipady=9
        )

        tk.Button(
            bottom,
            text="GENERATE RECEIPT",
            font=("Arial", 9, "bold"),
            bg="#202020",
            fg="white",
            relief="flat",
            command=self.generate_receipt
        ).pack(
            side="right",
            fill="x",
            expand=True,
            padx=(5, 0),
            ipady=9
        )

    # ---------------- ADD ITEM ----------------

    def add_item(self):

        name = self.item_entry.get().strip()
        price = self.price_entry.get().strip()
        quantity = self.quantity_entry.get().strip()

        if not name or not price or not quantity:
            messagebox.showwarning(
                "Missing Information",
                "Please enter item name, price and quantity."
            )
            return

        try:
            price = float(price)
            quantity = int(quantity)

            if price <= 0 or quantity <= 0:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Enter a valid price and quantity."
            )
            return

        self.cart.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })

        self.item_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

        self.update_cart()

    # ---------------- CART ----------------

    def update_cart(self):

        for widget in self.cart_frame.winfo_children():
            widget.destroy()

        if not self.cart:

            tk.Label(
                self.cart_frame,
                text="Your cart is empty",
                font=("Arial", 11),
                fg="#999999",
                bg="white"
            ).pack(pady=50)

            return

        for item in self.cart:

            row = tk.Frame(
                self.cart_frame,
                bg="white"
            )
            row.pack(
                fill="x",
                padx=12,
                pady=8
            )

            total = item["price"] * item["quantity"]

            tk.Label(
                row,
                text=item["name"],
                font=("Arial", 10, "bold"),
                bg="white",
                fg="#202020"
            ).pack(side="left")

            tk.Label(
                row,
                text=f'{item["quantity"]} × ₹{item["price"]:.2f}',
                font=("Arial", 9),
                bg="white",
                fg="#777777"
            ).pack(side="left", padx=10)

            tk.Label(
                row,
                text=f"₹{total:.2f}",
                font=("Arial", 10, "bold"),
                bg="white",
                fg="#202020"
            ).pack(side="right")

    # ---------------- CLEAR ----------------

    def clear_cart(self):

        self.cart.clear()
        self.update_cart()

    # ---------------- RECEIPT ----------------

    def generate_receipt(self):

        if not self.cart:

            messagebox.showwarning(
                "Empty Cart",
                "Add at least one item before generating a receipt."
            )
            return

        receipt = tk.Toplevel(self.root)
        receipt.title("Receipt")
        receipt.geometry("350x600")
        receipt.resizable(False, False)
        receipt.configure(bg="#d9d9d9")

        # Receipt paper
        paper = tk.Frame(
            receipt,
            bg="#fffdf5"
        )
        paper.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        tk.Label(
            paper,
            text="✦  MINI MART  ✦",
            font=("Courier New", 16, "bold"),
            bg="#fffdf5",
            fg="#111111"
        ).pack(pady=(20, 3))

        tk.Label(
            paper,
            text="YOUR SHOPPING RECEIPT",
            font=("Courier New", 8),
            bg="#fffdf5",
            fg="#555555"
        ).pack()

        tk.Label(
            paper,
            text="-" * 32,
            font=("Courier New", 9),
            bg="#fffdf5",
            fg="#111111"
        ).pack(pady=8)

        items_frame = tk.Frame(
            paper,
            bg="#fffdf5"
        )
        items_frame.pack(
            fill="x",
            padx=20
        )

        subtotal = 0

        for item in self.cart:

            item_total = item["price"] * item["quantity"]
            subtotal += item_total

            name = item["name"][:14]

            line = (
                f"{name:<14}"
                f"{item['quantity']:>3} "
                f"₹{item_total:>7.2f}"
            )

            tk.Label(
                items_frame,
                text=line,
                font=("Courier New", 9),
                bg="#fffdf5",
                fg="#111111",
                anchor="w"
            ).pack(
                fill="x",
                pady=2
            )

        # Calculations
        discount = 0

        if subtotal >= 2000:
            discount = subtotal * 0.10
        elif subtotal >= 1000:
            discount = subtotal * 0.05

        tax = (subtotal - discount) * 0.05
        final_total = subtotal - discount + tax

        tk.Label(
            paper,
            text="-" * 32,
            font=("Courier New", 9),
            bg="#fffdf5",
            fg="#111111"
        ).pack(pady=8)

        totals = tk.Frame(
            paper,
            bg="#fffdf5"
        )
        totals.pack(
            fill="x",
            padx=25
        )

        self.receipt_line(
            totals,
            "Subtotal",
            subtotal
        )

        self.receipt_line(
            totals,
            "Discount",
            -discount
        )

        self.receipt_line(
            totals,
            "Tax (5%)",
            tax
        )

        tk.Label(
            paper,
            text="-" * 32,
            font=("Courier New", 9),
            bg="#fffdf5",
            fg="#111111"
        ).pack(pady=8)

        tk.Label(
            paper,
            text=f"TOTAL     ₹{final_total:.2f}",
            font=("Courier New", 13, "bold"),
            bg="#fffdf5",
            fg="#111111"
        ).pack()

        tk.Label(
            paper,
            text="\nThank you for shopping!\n"
                 "Please visit again :)",
            font=("Courier New", 9),
            bg="#fffdf5",
            fg="#555555"
        ).pack(pady=15)

        tk.Button(
            paper,
            text="CLOSE",
            font=("Arial", 9, "bold"),
            bg="#202020",
            fg="white",
            relief="flat",
            command=receipt.destroy
        ).pack(
            pady=5,
            ipadx=25,
            ipady=5
        )

    def receipt_line(self, parent, label, amount):

        if amount < 0:
            value = f"-₹{abs(amount):.2f}"
        else:
            value = f"₹{amount:.2f}"

        row = tk.Frame(
            parent,
            bg="#fffdf5"
        )
        row.pack(fill="x")

        tk.Label(
            row,
            text=label,
            font=("Courier New", 9),
            bg="#fffdf5",
            fg="#111111"
        ).pack(side="left")

        tk.Label(
            row,
            text=value,
            font=("Courier New", 9),
            bg="#fffdf5",
            fg="#111111"
        ).pack(side="right")


# ---------------- RUN ----------------

root = tk.Tk()

app = ShoppingBill(root)

root.mainloop()