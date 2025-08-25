# Project1

```
p1/
├── main.py
├── .env
├── requirements.txt
└── README.md
```

## Description

This suite of tools extends the agent's capabilities to interact with common business systems, enabling automation and quick access to information.

- generate_sales_report(period, format_type, email_recipient): Creates comprehensive sales reports for specified periods (e.g., "monthly", "Q1 2024") in various formats and can email them out.
- query_customer_database(customer_id, email, last_orders_count): Retrieves detailed customer information and their recent order history using ID or email.
- create_jira_ticket(summary, description, assignee_email, priority): Automates the creation of new Jira tickets with specified details and assignments.
- lookup_product_inventory(product_name, product_sku, warehouse_id): Checks current stock levels for products, optionally within a specific warehouse.
- send_slack_message(channel, message): Facilitates sending messages to designated Slack channels or individual users.

## Requirements

- Python >= 3.13
- Dependencies:
  - langchain >= 0.3.27
  - langchain-openai >= 0.3.30
  - langgraph >= 0.6.5
  - python-dotenv >= 1.1.1

## Installation

1. Clone the repository
2. Create a virtual environment:
```sh
python -m venv env
source env/bin/activate  # On Unix/macOS
# or
.\env\Scripts\activate  # On Windows
```
3. Install dependencies:
```sh
pip install -e .
```

## Environment Setup

Create a `.env` file in the root directory and add your environment variables:
```sh
OPENAI_API_KEY=your_api_key_here
```