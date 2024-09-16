from typing import List, Dict
from src.repositories.ProductRepository import ProductRepository
from src.repositories.OrderRepository import OrderRepository
from src.entities.Product import Product
from src.entities.Order import Order

class ReportService:
    def __init__(self, product_repo: ProductRepository, order_repo: OrderRepository):
        self.product_repo = product_repo
        self.order_repo = order_repo

    def generate_low_stock_report(self, threshold: int) -> List[Product]:
        """Generate a list of products with stock below the threshold."""
        return [product for product in self.product_repo.products.values() if product.stock_level < threshold]

    def generate_sales_summary(self) -> Dict[str, float]:
        """Generate a summary of total sales."""
        total_sales = sum(order.calculate_total() for order in self.order_repo.orders.values() if order.status == "completed")
        return {"total_sales": total_sales}
