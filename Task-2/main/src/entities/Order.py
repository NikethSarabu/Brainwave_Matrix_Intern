from src.entities.Product import Product

class Order:
    def __init__(self, order_id: int, user_id: int):
        self.order_id = order_id
        self.user_id = user_id
        self.products = []  # List of (Product, quantity) tuples
        self.status = "pending"  # 'pending', 'completed', etc.

    def add_product(self, product: Product, quantity: int):
        """Add a product and its quantity to the order."""
        self.products.append((product, quantity))

    def remove_product(self, product_id: int):
        """Remove a product from the order by product_id."""
        self.products = [p for p in self.products if p[0].product_id != product_id]

    def calculate_total(self) -> float:
        """Calculate the total amount for the order."""
        return sum(product.price * quantity for product, quantity in self.products)

    def complete_order(self):
        """Complete the order and reduce stock levels."""
        for product, quantity in self.products:
            product.remove_stock(quantity)
        self.status = "completed"

    def __str__(self):
        return f"Order({self.order_id}, {len(self.products)} products, Status: {self.status})"
