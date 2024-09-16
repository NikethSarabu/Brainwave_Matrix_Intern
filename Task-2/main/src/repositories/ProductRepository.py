from typing import Dict
from src.entities.Product import Product

class ProductRepository:
    def __init__(self):
        self.products: Dict[int, Product] = {}

    def add(self, product: Product):
        self.products[product.product_id] = product

    def get(self, product_id: int) -> Product:
        return self.products.get(product_id)

    def delete(self, product_id: int):
        if product_id in self.products:
            del self.products[product_id]

    def update(self, product: Product):
        self.products[product.product_id] = product
