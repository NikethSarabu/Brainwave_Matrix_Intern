from src.services.OrderService import OrderService

class OrderController:
    def __init__(self, order_service: OrderService):
        self.order_service = order_service

    def create_order(self, order_id, user_id):
        try:
            order = self.order_service.create_order(order_id, user_id)
            return f"Order {order_id} created successfully."
        except ValueError as e:
            return f"Error: {str(e)}"

    def complete_order(self, order_id):
        try:
            self.order_service.complete_order(order_id)
            return f"Order {order_id} completed successfully."
        except ValueError as e:
            return f"Error: {str(e)}"

    def list_orders(self):
        orders = self.order_service.list_all_orders()
        return orders
