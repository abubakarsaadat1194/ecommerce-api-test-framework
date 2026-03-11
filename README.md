# E-commerce API Test Automation Framework

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pytest](https://img.shields.io/badge/Test%20Framework-Pytest-green)
![Requests](https://img.shields.io/badge/HTTP%20Client-Requests-orange)
![CI](https://github.com/abubakarsaadat1194/ecommerce-api-test-framework/actions/workflows/api-tests.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-blue)

A scalable **API test automation framework** built using **Python, Pytest, and Requests** to validate REST APIs of an e-commerce platform.
A scalable **API test automation framework** built using **Python, Pytest, and Requests** to validate REST APIs of an e-commerce platform.

The framework follows a **layered architecture (Client → Service → Test)** to ensure maintainability, reusability, and scalability for enterprise-level API testing.

It also includes **data factories, response schema validation, performance checks, and CI integration**.

---

# Features

• API automation using **Python + Pytest**

• **Layered architecture** for scalable test design

• **Reusable API client** for HTTP requests

• **Service layer abstraction** for business API logic

• **Schema validation** using **Pydantic models**

• **Dynamic test data generation** using **Faker**

• **Performance validation** for API response times

• **Mocked API responses** for stable CI pipelines

• **Parallel test execution** using **pytest-xdist**

• **Automated test reporting** using **pytest-html**

• **Continuous Integration pipeline** using **GitHub Actions**

---

# Project Architecture

    Ecommerce-API-Test-Framework
    │
    ├── clients
    │   └── api_client.py
    │
    ├── services
    │   ├── product_service.py
    │   ├── cart_service.py
    │   └── user_service.py
    │
    ├── factories
    │   ├── product_factory.py
    │   └── cart_factory.py
    │
    ├── models
    │   └── product_model.py
    │
    ├── utils
    │   ├── config.py
    │   └── performance.py
    │
    ├── tests
    │   ├── test_products.py
    │   ├── test_carts.py
    │   └── test_users.py
    │
    ├── pytest.ini
    ├── requirements.txt
    └── README.md

---

# Architecture Explanation

## API Client Layer

Handles **HTTP communication with APIs**.

File:

    clients/api_client.py

Responsible for:

• Sending GET / POST requests  
• Logging request details  
• Handling responses  

---

## Service Layer

Encapsulates **business API operations**.

Examples:

    ProductService.get_all_products()
    CartService.create_cart()
    UserService.get_user()

This separates **test logic from API endpoints**.

---

## Factory Layer

Generates **dynamic test data** using **Faker**.

Examples:

    ProductFactory.create()
    CartFactory.create()

Benefits:

• Avoids hardcoded data  
• Enables realistic testing scenarios  

---

## Model Layer

Validates **API response schemas** using **Pydantic**.

Example:

    validated_product = Product(**product)

Ensures:

• Correct data types  
• Required fields present  

---

## Utility Layer

Contains reusable helpers.

Examples:

    validate_response_time()
    BASE_URL configuration

Used across all tests.

---

## Test Layer

Contains **actual test cases** validating API behaviour.

Examples:

    test_get_all_products
    test_get_single_product
    test_create_product

Includes:

• Status code validation  
• Schema validation  
• Response time checks  

---

# Running Tests

Install dependencies:

    pip install -r requirements.txt

Run tests:

    pytest -v

Run tests in parallel:

    pytest -n 4

Generate HTML report:

    pytest --html=report.html

---

# Example Test Execution

    tests/test_products.py::test_get_all_products PASSED
    tests/test_products.py::test_get_single_product PASSED
    tests/test_products.py::test_create_product PASSED
    tests/test_carts.py::test_get_all_carts PASSED
    tests/test_users.py::test_get_all_users PASSED

---

# Continuous Integration

This project includes a **GitHub Actions pipeline** that automatically:

• Installs dependencies  
• Executes the API test suite  
• Generates test reports  

CI configuration:

    .github/workflows/api-tests.yml

The pipeline runs on every **push or pull request**.

---

# Technologies Used

Python  
Pytest  
Requests  
Faker  
Pydantic  
pytest-xdist  
pytest-html  
GitHub Actions  

---

# Key Testing Concepts Implemented

• API Automation  
• Layered Test Architecture  
• Data-driven testing  
• Response schema validation  
• Performance validation  
• CI/CD automation  
• Mocked API testing for CI stability  

---

# Author

**Abu Bakar Saadat**

Software Quality Assurance Engineer  
Munich, Germany

LinkedIn  
https://linkedin.com/in/abu-bakar-saadat-b142bb103

GitHub  
https://github.com/abubakarsaadat1194
