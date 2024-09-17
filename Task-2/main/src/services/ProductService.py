from src.repositories.ProductRepository import ProductRepository
from src.entities.Product import Product

class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def add_product(self, product: Product):
        self.repository.add(product)

    def get_product(self, product_id: int) -> Product:
        return self.repository.get(product_id)

    def delete_product(self, product_id: int):
        self.repository.delete(product_id)

    def update_product(self, product: Product):
        self.repository.update(product)

    def list_all_products(self):
        return self.repository.get_all_products()