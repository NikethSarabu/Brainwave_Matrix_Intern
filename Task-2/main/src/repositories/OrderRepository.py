from typing import Dict
from src.entities.Order import Order

class OrderRepository:
    def __init__(self):
        self.orders: Dict[int, Order] = {}

    def add(self, order: Order):
        self.orders[order.order_id] = order

    def get(self, order_id: int) -> Order:
        return self.orders.get(order_id)

    def delete(self, order_id: int):
        if order_id in self.orders:
            del self.orders[order_id]

    def update(self, order: Order):
        self.orders[order.order_id] = order
