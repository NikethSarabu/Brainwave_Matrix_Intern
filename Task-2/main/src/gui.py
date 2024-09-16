import tkinter as tk
from tkinter import messagebox, simpledialog
from src.repositories.ProductRepository import ProductRepository
from src.repositories.OrderRepository import OrderRepository
from src.repositories.UserRepository import UserRepository
from src.services.ProductService import ProductService
from src.services.OrderService import OrderService
from src.services.UserService import UserService
from src.services.AuthenticationService import AuthenticationService
from src.services.ReportService import ReportService
from src.entities.Product import Product
from src.entities.Order import Order
from src.entities.User import User

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")

        self.product_repo = ProductRepository()
        self.order_repo = OrderRepository()
        self.user_repo = UserRepository()

        self.product_service = ProductService(self.product_repo)
        self.order_service = OrderService(self.order_repo)
        self.user_service = UserService(self.user_repo)
        self.auth_service = AuthenticationService(self.user_repo)
        self.report_service = ReportService(self.product_repo, self.order_repo)

        self.create_widgets()

    def create_widgets(self):
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(pady=10)

        tk.Label(self.login_frame, text="Username:").grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.login_frame, text="Password:").grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(self.login_frame, show='*')
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(self.login_frame, text="Login", command=self.login).grid(row=2, columnspan=2, pady=10)

        self.main_frame = tk.Frame(self.root)
        
        self.product_button = tk.Button(self.main_frame, text="Manage Products", command=self.manage_products)
        self.product_button.pack(pady=5)

        self.user_button = tk.Button(self.main_frame, text="Manage Users", command=self.manage_users)
        self.user_button.pack(pady=5)

        self.report_button = tk.Button(self.main_frame, text="Generate Reports", command=self.generate_reports)
        self.report_button.pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            self.auth_service.authenticate(username, password)
            self.login_frame.pack_forget()
            self.main_frame.pack(pady=10)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def manage_products(self):
        action = simpledialog.askstring("Product Management", "Enter 'add', 'update', 'delete' or 'view':").strip().lower()
        if action == 'add':
            self.add_product()
        elif action == 'update':
            self.update_product()
        elif action == 'delete':
            self.delete_product()
        elif action == 'view':
            self.view_product()
        else:
            messagebox.showwarning("Warning", "Invalid action")

    def manage_users(self):
        action = simpledialog.askstring("User Management", "Enter 'add', 'update', 'delete' or 'view':").strip().lower()
        if action == 'add':
            self.add_user()
        elif action == 'update':
            self.update_user()
        elif action == 'delete':
            self.delete_user()
        elif action == 'view':
            self.view_user()
        else:
            messagebox.showwarning("Warning", "Invalid action")

    def generate_reports(self):
        report_type = simpledialog.askstring("Report", "Enter 'low_stock' or 'sales_summary':").strip().lower()
        if report_type == 'low_stock':
            self.show_low_stock_report()
        elif report_type == 'sales_summary':
            self.show_sales_summary()
        else:
            messagebox.showwarning("Warning", "Invalid report type")

    def add_product(self):
        product_id = simpledialog.askinteger("Add Product", "Enter Product ID:")
        name = simpledialog.askstring("Add Product", "Enter Product Name:")
        description = simpledialog.askstring("Add Product", "Enter Product Description:")
        price = simpledialog.askfloat("Add Product", "Enter Product Price:")
        stock_level = simpledialog.askinteger("Add Product", "Enter Stock Level:")
        product = Product(product_id, name, description, price, stock_level)
        self.product_service.add_product(product)
        messagebox.showinfo("Success", "Product added successfully")

    def update_product(self):
        product_id = simpledialog.askinteger("Update Product", "Enter Product ID:")
        product = self.product_service.get_product(product_id)
        if product:
            name = simpledialog.askstring("Update Product", "Enter New Product Name:", initialvalue=product.name)
            description = simpledialog.askstring("Update Product", "Enter New Product Description:", initialvalue=product.description)
            price = simpledialog.askfloat("Update Product", "Enter New Product Price:", initialvalue=product.price)
            stock_level = simpledialog.askinteger("Update Product", "Enter New Stock Level:", initialvalue=product.stock_level)
            product.name = name
            product.description = description
            product.price = price
            product.stock_level = stock_level
            self.product_service.update_product(product)
            messagebox.showinfo("Success", "Product updated successfully")
        else:
            messagebox.showwarning("Warning", "Product not found")

    def delete_product(self):
        product_id = simpledialog.askinteger("Delete Product", "Enter Product ID:")
        self.product_service.delete_product(product_id)
        messagebox.showinfo("Success", "Product deleted successfully")

    def view_product(self):
        product_id = simpledialog.askinteger("View Product", "Enter Product ID:")
        product = self.product_service.get_product(product_id)
        if product:
            info = f"ID: {product.product_id}\nName: {product.name}\nDescription: {product.description}\nPrice: {product.price}\nStock Level: {product.stock_level}"
            messagebox.showinfo("Product Information", info)
        else:
            messagebox.showwarning("Warning", "Product not found")

    def add_user(self):
        user_id = simpledialog.askinteger("Add User", "Enter User ID:")
        username = simpledialog.askstring("Add User", "Enter Username:")
        password = simpledialog.askstring("Add User", "Enter Password:")
        role = simpledialog.askstring("Add User", "Enter Role:")
        user = User(user_id, username, password, role)
        self.user_service.add_user(user)
        messagebox.showinfo("Success", "User added successfully")

    def update_user(self):
        user_id = simpledialog.askinteger("Update User", "Enter User ID:")
        user = self.user_service.get_user(user_id)
        if user:
            username = simpledialog.askstring("Update User", "Enter New Username:", initialvalue=user.username)
            password = simpledialog.askstring("Update User", "Enter New Password:", initialvalue=user.password)
            role = simpledialog.askstring("Update User", "Enter New Role:", initialvalue=user.role)
            user.username = username
            user.password = password
            user.role = role
            self.user_service.update_user(user)
            messagebox.showinfo("Success", "User updated successfully")
        else:
            messagebox.showwarning("Warning", "User not found")

    def delete_user(self):
        user_id = simpledialog.askinteger("Delete User", "Enter User ID:")
        self.user_service.delete_user(user_id)
        messagebox.showinfo("Success", "User deleted successfully")

    def view_user(self):
        user_id = simpledialog.askinteger("View User", "Enter User ID:")
        user = self.user_service.get_user(user_id)
        if user:
            info = f"ID: {user.user_id}\nUsername: {user.username}\nRole: {user.role}"
            messagebox.showinfo("User Information", info)
        else:
            messagebox.showwarning("Warning", "User not found")

    def show_low_stock_report(self):
        threshold = simpledialog.askinteger("Low Stock Report", "Enter Stock Threshold:")
        low_stock_products = self.report_service.generate_low_stock_report(threshold)
        report = "\n".join([f"ID: {p.product_id}, Name: {p.name}, Stock Level: {p.stock_level}" for p in low_stock_products])
        messagebox.showinfo("Low Stock Report", report if report else "No low stock items.")

    def show_sales_summary(self):
        sales_summary = self.report_service.generate_sales_summary()
        messagebox.showinfo("Sales Summary", f"Total Sales: {sales_summary['total_sales']:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
