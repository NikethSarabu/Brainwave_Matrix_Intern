# Inventory Management System

## Overview
This project is an Inventory Management System built with Python, Tkinter for the GUI and follows OOP and SOLID principles. It allows users to manage inventory, including adding, editing, and deleting products and also provides user authentication and password management.

## File Structure
```
Task-2/
│
├─ main/
│   ├── src/
│   │   ├── entities/
│   │   │   ├── __init__.py
│   │   │   ├── Product.py
│   │   │   └── User.py
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   ├── ProductRepository.py
│   │   │   └── UserRepository.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── ProductService.py
│   │   │   └── UserService.py
│   │   ├── controller/
│   │   │   ├── __init__.py
│   │   │   ├── ProductController.py
│   │   │   └── UserController.py
│   ├── __init__.py
│   ├── gui.py
│   ├── main.py
├── README.md
└── run.sh
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/NikethSarabu/Brainwave_Matrix_Intern/
   ```

2. Navigate to the project directory:
   ```
   cd Task-2
   ```

## Usage
1. Run the application:
    ```bash
    bash run.sh
    ```
    or 
    ```bash
    python main/main.py
    ```

2. The GUI will prompt for user login. Create a new user or use the default admin credentials:
   - Username: `admin`
   - Password: `1234`

3. Once logged in, you can manage products and users through the interface.

## Features
- **User Authentication:** Log in with existing users and create new users.
- **Product Management:** Add, update, delete, and view products.
- **Password Management:** Change user passwords.

