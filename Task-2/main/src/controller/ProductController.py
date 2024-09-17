from src.entities.Product import Product
from src.services.ProductService import ProductService

class ProductController:
    def __init__(self, product_service: ProductService):
        self.product_service = product_service

    def add_product(self, product_id, name, description, price, stock_level):
        try:
            product = Product(product_id, name, description, price, stock_level)
            self.product_service.add_product(product)
            return f"Product {name} added successfully."
        except ValueError as e:
            return f"Error: {str(e)}"

    def update_product(self, product_id, name, description, price, stock_level):
        try:
            product = Product(product_id, name, description, price, stock_level) 
            self.product_service.update_product(product)
            return f"Product {name} updated successfully."
        except ValueError as e:
            return f"Error: {str(e)}"

    def delete_product(self, product_id):
        try:
            self.product_service.delete_product(product_id)
            return f"Product {product_id} deleted successfully."
        except ValueError as e:
            return f"Error: {str(e)}"

    def list_products(self):
        products = self.product_service.list_all_products()
        return products
