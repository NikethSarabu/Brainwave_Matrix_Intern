class Product:
    def __init__(self, product_id: int, name: str, description: str, price: float, stock_level: int):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock_level = stock_level

    def add_stock(self, quantity: int):
        """Increase stock level."""
        self.stock_level += quantity

    def remove_stock(self, quantity: int):
        """Decrease stock level. Raise an error if quantity is higher than stock level."""
        if quantity > self.stock_level:
            raise ValueError("Insufficient stock to remove")
        self.stock_level -= quantity

    def update_price(self, new_price: float):
        """Update the price of the product."""
        self.price = new_price

    def __str__(self):
        return f"Product({self.product_id}, {self.name}, {self.stock_level} in stock, ${self.price})"
