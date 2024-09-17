import tkinter as tk
from tkinter import messagebox

from src.services.ProductService import ProductService
from src.services.UserService import UserService
from src.repositories.ProductRepository import ProductRepository
from src.repositories.UserRepository import UserRepository
from src.controller.ProductController import ProductController
from src.controller.UserController import UserController

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        
        self.product_repo = ProductRepository()
        self.user_repo = UserRepository()

        self.product_service = ProductService(self.product_repo)
        self.user_service = UserService(self.user_repo)

        self.product_controller = ProductController(self.product_service)
        self.user_controller = UserController(self.user_service)

        self.current_user = None

        self.setup_login()
        self.initialize_data()

    def setup_login(self):
        self.clear_gui()

        tk.Label(self.root, text="Username").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Password").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.grid(row=1, column=1)

        login_button = tk.Button(self.root, text="Login", command=self.authenticate_user)
        login_button.grid(row=2, column=1)

        create_user_button = tk.Button(self.root, text="Create User", command=self.create_user)
        create_user_button.grid(row=3, column=1)

    def clear_gui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def authenticate_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            self.current_user = self.user_controller.authenticate(username, password)
            self.setup_main_gui()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def create_user(self):
        self.clear_gui()
        tk.Label(self.root, text="User ID").grid(row=0, column=0)
        self.user_id_entry = tk.Entry(self.root)
        self.user_id_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Username").grid(row=1, column=0)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Password").grid(row=2, column=0)
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Role").grid(row=3, column=0)
        self.role_entry = tk.Entry(self.root)
        self.role_entry.grid(row=3, column=1)

        create_button = tk.Button(self.root, text="Create User", command=self.add_user)
        create_button.grid(row=4, column=1)

        cancel_button = tk.Button(self.root, text="Cancel", command=self.setup_login)
        cancel_button.grid(row=5, column=1)

    def add_user(self):
        user_id = self.user_id_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_entry.get()
        try:
            result = self.user_controller.add_user(user_id, username, password, role)
            messagebox.showinfo("Result", result)
            self.setup_login()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def setup_main_gui(self):
        self.clear_gui()

        tk.Label(self.root, text="Product Management").grid(row=0, column=0, columnspan=2)

        tk.Label(self.root, text="Product ID").grid(row=1, column=0)
        self.product_id_entry = tk.Entry(self.root)
        self.product_id_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Product Name").grid(row=2, column=0)
        self.product_name_entry = tk.Entry(self.root)
        self.product_name_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Description").grid(row=3, column=0)
        self.product_desc_entry = tk.Entry(self.root)
        self.product_desc_entry.grid(row=3, column=1)

        tk.Label(self.root, text="Price").grid(row=4, column=0)
        self.product_price_entry = tk.Entry(self.root)
        self.product_price_entry.grid(row=4, column=1)

        tk.Label(self.root, text="Stock Level").grid(row=5, column=0)
        self.product_stock_entry = tk.Entry(self.root)
        self.product_stock_entry.grid(row=5, column=1)

        add_product_button = tk.Button(self.root, text="Add Product", command=self.add_product)
        add_product_button.grid(row=6, column=1)

        update_product_button = tk.Button(self.root, text="Update Product", command=self.update_product)
        update_product_button.grid(row=7, column=1)

        delete_product_button = tk.Button(self.root, text="Delete Product", command=self.delete_product)
        delete_product_button.grid(row=8, column=1)

        view_products_button = tk.Button(self.root, text="View Products", command=self.view_products)
        view_products_button.grid(row=9, column=1)

        change_password_button = tk.Button(self.root, text="Change Password", command=self.change_password)
        change_password_button.grid(row=10, column=1)

    def add_product(self):
        product_id = self.product_id_entry.get()
        name = self.product_name_entry.get()
        description = self.product_desc_entry.get()
        price = float(self.product_price_entry.get())
        stock_level = int(self.product_stock_entry.get())
        try:
            result = self.product_controller.add_product(product_id, name, description, price, stock_level)
            messagebox.showinfo("Result", result)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_product(self):
        product_id = self.product_id_entry.get()
        name = self.product_name_entry.get()
        description = self.product_desc_entry.get()
        price = float(self.product_price_entry.get())
        stock_level = int(self.product_stock_entry.get())
        try:
            result = self.product_controller.update_product(product_id, name, description, price, stock_level)
            messagebox.showinfo("Result", result)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_product(self):
        product_id = self.product_id_entry.get()
        try:
            result = self.product_controller.delete_product(product_id)
            messagebox.showinfo("Result", result)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def view_products(self):
        try:
            products = self.product_controller.list_products()
            product_list = "\n".join([f"{p.product_id} - {p.name}: {p.stock_level} in stock" for p in products])
            messagebox.showinfo("Product List", product_list)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def change_password(self):
        self.clear_gui()
        tk.Label(self.root, text="New Password").grid(row=0, column=0)
        self.new_password_entry = tk.Entry(self.root, show='*')
        self.new_password_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Confirm Password").grid(row=1, column=0)
        self.confirm_password_entry = tk.Entry(self.root, show='*')
        self.confirm_password_entry.grid(row=1, column=1)

        change_button = tk.Button(self.root, text="Change Password", command=self.update_password)
        change_button.grid(row=2, column=1)

        cancel_button = tk.Button(self.root, text="Cancel", command=self.setup_main_gui)
        cancel_button.grid(row=3, column=1)

    def update_password(self):
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        if new_password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return
        try:
            self.user_controller.update_user(self.current_user.user_id, self.current_user.username, new_password, self.current_user.role)
            messagebox.showinfo("Result", "Password updated successfully.")
            self.setup_main_gui()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def initialize_data(self):
        try:
            self.user_controller.add_user("0", "admin", "1234", "admin")
            self.product_controller.add_product("1", "Apple", "Fresh apple", 1.0, 100)
            self.product_controller.add_product("2", "Banana", "Ripe banana", 0.5, 150)
        except ValueError as e:
            print(f"Initialization error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
