from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import datetime
import json
import requests

load_dotenv()

@tool
def generate_sales_report(period: str, format_type: str = "PDF", email_recipient: str = "<email>") -> str:
    """
    Generates a sales report for a specified period and can optionally email it.
    Args:
        period (str): The reporting period (e.g., "daily", "weekly", "monthly", "Q1 2024").
        format_type (str): The desired report format (e.g., "PDF", "CSV", "Excel"). Default is PDF.
        email_recipient (str): Optional email address to send the report to.
    """
    print(f"Tool 'generate_sales_report' called for period: {period}, format: {format_type}.")
    
    # --- Placeholder: Replace with actual sales report generation logic ---
    report_data = f"Simulated Sales Report for {period}:\n" \
                  f"Total Sales: $1,234,567\n" \
                  f"Top Product: Widget X (Sales: $500,000)\n"
    
    if email_recipient:
        print(f"Simulating emailing {format_type} report to {email_recipient}...")
        report_data += f"Report sent to {email_recipient}."
    else:
        print("Simulating report generation without emailing.")
        report_data += "Report generated successfully."
    # --- End Placeholder ---
    
    return report_data

@tool
def query_customer_database(customer_id: str = None, email: str = None, last_orders_count: int = 0) -> str:
    """
    Retrieves customer information from the database. Requires either customer_id or email.
    Can also fetch a specified number of recent orders for the customer.
    Args:
        customer_id (str): The ID of the customer.
        email (str): The email address of the customer.
        last_orders_count (int): Number of recent orders to fetch. Default is 0 (no orders).
    """
    print(f"Tool 'query_customer_database' called for customer_id: {customer_id}, email: {email}, last_orders_count: {last_orders_count}.")

    if not customer_id and not email:
        return "Error: Either 'customer_id' or 'email' must be provided."

    # --- Placeholder: Replace with actual database query logic ---
    customer_info = {
        "id": customer_id if customer_id else "CUST_987",
        "name": "Jane Doe",
        "email": email if email else "jane.doe@example.com",
        "address": "123 Main St, Anytown",
        "status": "Active"
    }

    orders = []
    if last_orders_count > 0:
        for i in range(last_orders_count):
            order_id = f"ORD_100{5-i}"
            order_date = (datetime.date.today() - datetime.timedelta(days=i*7)).strftime("%Y-%m-%d")
            orders.append({"order_id": order_id, "date": order_date, "amount": f"${100 + i*10}"})
    # --- End Placeholder ---

    response = f"Customer Info:\n{json.dumps(customer_info, indent=2)}\n"
    if orders:
        response += f"Last {last_orders_count} Orders:\n{json.dumps(orders, indent=2)}\n"
    
    return response

@tool
def create_jira_ticket(summary: str, description: str = "", assignee_email: str = None, priority: str = "Medium") -> str:
    """
    Creates a new Jira ticket.
    Args:
        summary (str): A concise summary of the issue/task.
        description (str): A detailed description of the issue/task.
        assignee_email (str): Optional email of the assignee.
        priority (str): The priority of the ticket (e.g., "Low", "Medium", "High", "Critical").
    """
    print(f"Tool 'create_jira_ticket' called for summary: '{summary}', assignee: {assignee_email}.")

    # --- Placeholder: Replace with actual Jira API call ---
    # Example fields for a Jira API request
    jira_fields = {
        "project": {"key": "PROJ"}, # Replace with your Jira project key
        "summary": summary,
        "description": description if description else "No description provided.",
        "issuetype": {"name": "Task"}, # Or "Bug", "Story", etc.
        "priority": {"name": priority}
    }
    if assignee_email:
        jira_fields["assignee"] = {"emailAddress": assignee_email}

    # Simulate Jira Ticket ID
    new_ticket_id = f"PROJ-{datetime.datetime.now().microsecond % 10000}"
    print(f"Simulating Jira ticket creation with payload: {json.dumps(jira_fields, indent=2)}")
  
    response = requests.post(JIRA_API_URL, json=jira_fields, auth=(JIRA_USERNAME, JIRA_API_TOKEN))
    if response.status_code == 201:
        new_ticket_id = response.json().get("key")
    else:
        return f"Failed to create Jira ticket: {response.text}"
    #--- End Placeholder ---

    return f"Jira ticket '{new_ticket_id}' created successfully with summary: '{summary}'."
    
@tool
def lookup_product_inventory(product_name: str = None, product_sku: str = None, warehouse_id: str = None) -> str:
    """
    Looks up the current inventory level for a product. Requires product_name or product_sku.
    Can specify a warehouse.
    Args:
        product_name (str): The name of the product.
        product_sku (str): The SKU of the product.
        warehouse_id (str): The ID of the warehouse to check. Optional.
    """
    print(f"Tool 'lookup_product_inventory' called for name: {product_name}, SKU: {product_sku}, warehouse: {warehouse_id}.")

    if not product_name and not product_sku:
        return "Error: Either 'product_name' or 'product_sku' must be provided."

    # --- Placeholder: Replace with actual inventory system query ---
    stock_level = "Unknown"
    if product_name and "Widget A" in product_name:
        stock_level = "500 units"
        if warehouse_id:
            stock_level = "150 units in WH-001" if warehouse_id == "WH-001" else "350 units in WH-002"
    elif product_sku == "SKU-XYZ":
        stock_level = "1000 units"
    else:
        stock_level = "Not Found or Out of Stock."
    # --- End Placeholder ---

    location_info = f" in warehouse {warehouse_id}" if warehouse_id else ""
    return f"Inventory for {product_name or product_sku}{location_info}: {stock_level}."

@tool
def send_slack_message(channel: str, message: str) -> str:
    """
    Sends a message to a specific Slack channel or user.
    Args:
        channel (str): The Slack channel name (e.g., "#general") or user ID (e.g., "@johndoe").
        message (str): The content of the message.
    """
    print(f"Tool 'send_slack_message' called for channel: {channel}, message: '{message}'.")

     #--- Placeholder: Replace with actual Slack API call ---
     #You would typically use a Slack Bot Token and API here
    SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
    slack_api_url = "https://slack.com/api/chat.postMessage"
    headers = {"Authorization": f"Bearer {SLACK_BOT_TOKEN}", "Content-type": "application/json"}
    payload = {"channel": channel, "text": message}
    response = requests.post(slack_api_url, headers=headers, data=json.dumps(payload))
    
    if response.json().get("ok"):
        return f"Message successfully sent to {channel}."
    else:
        return f"Failed to send Slack message: {response.json().get('error', 'Unknown error')}."
    #--- End Placeholder ---
    
    return f"Simulated: Message '{message}' sent to Slack channel/user '{channel}'."


def main():
    model = ChatOpenAI(temperature=0)
    
    tools = [
        generate_sales_report, query_customer_database, create_jira_ticket,
        lookup_product_inventory, send_slack_message
    ]
    agent_executor = create_react_agent(model, tools) # [1]
    
    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to generate reports, query customers, create Jira tickets, lookup inventory, or send Slack messages.")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input == "quit":
            break
        
        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()
        
if __name__ == "__main__":
    main()