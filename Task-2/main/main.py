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

def main():
    product_repo = ProductRepository()
    order_repo = OrderRepository()
    user_repo = UserRepository()

    product_service = ProductService(product_repo)
    order_service = OrderService(order_repo)
    user_service = UserService(user_repo)
    auth_service = AuthenticationService(user_repo)
    report_service = ReportService(product_repo, order_repo)

    admin = User(user_id=1, username='admin', password='admin123', role='admin')
    user_service.add_user(admin)

    try:
        authenticated_user = auth_service.authenticate('admin', 'admin123')
        print(f"Authenticated: {authenticated_user}")
    except ValueError as e:
        print(e)
        return

    product1 = Product(product_id=1, name='Laptop', description='i7 laptop', price=1_20_000.00, stock_level=10)
    product_service.add_product(product1)

    order = Order(order_id=1, user_id=1)
    order.add_product(product1, 2)
    order_service.create_order(order)
    order_service.complete_order(order)

    low_stock_report = report_service.generate_low_stock_report(threshold=5)
    print("Low Stock Report:")
    for product in low_stock_report:
        print(f"ID: {product.product_id}, Name: {product.name}, Stock Level: {product.stock_level}")

    sales_summary = report_service.generate_sales_summary()
    print(f"Sales Summary: {sales_summary['total_sales']:.2f}")

if __name__ == "__main__":
    main()
