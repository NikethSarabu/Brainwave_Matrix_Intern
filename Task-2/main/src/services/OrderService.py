from src.repositories.OrderRepository import OrderRepository
from src.entities.Order import Order

class OrderService:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def create_order(self, order: Order):
        self.repository.add(order)

    def get_order(self, order_id: int) -> Order:
        return self.repository.get(order_id)

    def cancel_order(self, order_id: int):
        self.repository.delete(order_id)

    def complete_order(self, order: Order):
        order.complete_order()
        self.repository.update(order)
