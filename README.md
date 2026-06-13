# E-Commerce Automation Testing Framework

An automated UI testing framework built using **Python**, **Pytest**, and **Playwright**. This suite implements a structured **Page Object Model (POM)** design to validate the core user journeys of an e-commerce storefront, utilizing modern testing plugins for parallel execution and visual reporting.

## Architecture Design

* **pages/**: Pure Page Object components housing descriptive, isolated element locators and clean user actions.
* **test/**: Pytest execution scripts running structured end-to-end user validations against core business paths.
* **utils/ & test_data/**: Decoupled configurations separating registration datasets and application environments from core script files.

```text
Ecommerce/
│
├── pages/
│   ├── cart.py
│   ├── checkout.py
│   └── contact_us.py
│
├── test/
│   ├── conftest.py
│   ├── test_cart_page.py
│   └── test_checkout_page.py
│
├── utils/
│   ├── dummy_upload.txt
│   └── test_data.py
│
├── pytest.ini
├── requirements.txt
└── README.md

## Automated BAU Flow Coverage
This framework targets high-value Business-As-Usual (BAU) flows to ensure stability across core revenue-generating functionalities:
- **User Management**: Registration, Account Login, Logout, and Clean Teardown (Account Deletion).
- **Shopping Cart Mechanics**: Adding product quantities to cart, row calculation validation, and item deletion.
- **Product Discovery**: Left-sidebar category filtering (Men/Women sub-categories) and product detail inspection.
- **Checkout Funnel**: Comment submission, billing details verification, and transaction placement execution.

## Getting Started
1. Clone the repository: `git clone https://github.com/GlennSindingan/ecommerce-playwright-tests.git`
2. Create and source a virtual environment: `python -m venv .venv`
3. Install project dependencies: `pip install -r requirements.txt`
4. Initialize your local browser binaries: `playwright install`
5. Execute the validation suite: `pytest --headed`
