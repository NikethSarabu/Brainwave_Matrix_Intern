import unittest
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

class TestInventoryManagementSystem(unittest.TestCase):

    def setUp(self):
        self.product_repo = ProductRepository()
        self.order_repo = OrderRepository()
        self.user_repo = UserRepository()

        self.product_service = ProductService(self.product_repo)
        self.order_service = OrderService(self.order_repo)
        self.user_service = UserService(self.user_repo)
        self.auth_service = AuthenticationService(self.user_repo)
        self.report_service = ReportService(self.product_repo, self.order_repo)

    def test_user_authentication(self):
        user = User(user_id=1, username='testuser', password='password', role='admin')
        self.user_service.add_user(user)
        authenticated_user = self.auth_service.authenticate('testuser', 'password')
        self.assertEqual(authenticated_user.username, 'testuser')

    def test_product_management(self):
        product = Product(product_id=1, name='Test Product', description='Test', price=100.0, stock_level=10)
        self.product_service.add_product(product)
        retrieved_product = self.product_service.get_product(1)
        self.assertEqual(retrieved_product.name, 'Test Product')

    def test_order_processing(self):
        product = Product(product_id=1, name='Test Product', description='Test', price=100.0, stock_level=10)
        self.product_service.add_product(product)

        order = Order(order_id=1, user_id=1)
        order.add_product(product, 2)
        self.order_service.create_order(order)
        self.order_service.complete_order(order)

        self.assertEqual(product.stock_level, 8)

    def test_report_generation(self):
        product = Product(product_id=1, name='Test Product', description='Test', price=100.0, stock_level=10)
        self.product_service.add_product(product)

        order = Order(order_id=1, user_id=1)
        order.add_product(product, 2)
        self.order_service.create_order(order)
        self.order_service.complete_order(order)

        low_stock_report = self.report_service.generate_low_stock_report(threshold=5)
        self.assertIn(product, low_stock_report)

        sales_summary = self.report_service.generate_sales_summary()
        self.assertEqual(sales_summary['total_sales'], 200.0)

if __name__ == "__main__":
    unittest.main()

