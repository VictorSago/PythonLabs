
# ==========================================================
# Lab 5 Challenge
# ==========================================================

# --- Part 1 - Products and customers ---
products = [
    {"name": "Wireless Mouse", "price": 25.99, "category": "Electronics"},
    {"name": "Mechanical Keyboard", "price": 89.50, "category": "Electronics"},
    {"name": "USB-C Hub", "price": 34.00, "category": "Electronics"},
    {"name": "Desk Lamp", "price": 42.75, "category": "Home"},
    {"name": "Ceramic Mug", "price": 12.00, "category": "Home"},
    {"name": "Notebook", "price": 6.50, "category": "Stationery"},
    {"name": "Fountain Pen", "price": 18.25, "category": "Stationery"},
    {"name": "Backpack", "price": 59.99, "category": "Accessories"},
]

customers = [
    {"name": "Anna Andersson", "email": "anna.andersson@example.com", "customer_id": "C001"},
    {"name": "David Kim", "email": "david.kim@example.com", "customer_id": "C002"},
    {"name": "Sara Nilsson", "email": "sara.nilsson@example.com", "customer_id": "C003"},
    {"name": "Leo Martins", "email": "leo.martins@example.com", "customer_id": "C004"},
    {"name": "Mia Fischer", "email": "mia.fischer@example.com", "customer_id": "C005"},
]

# --- Part 2 - Create orders ---
def create_order(order_id, customer, *order_products, **order_options):
    """Create a structured order.

    order_id and customer are required, and *order_products accepts one or
    more products directly (an order must contain at least one). Optional
    order information is accepted through **order_options - only the options
    that are actually passed end up in the order.
    """
    order = {
        "order_id": order_id,
        "customer": customer,
        "products": list(order_products),
    }
    order.update(order_options)
    return order


order_1 = create_order(
    "ORD-1001", customers[0], products[0],
    shipping="standard",
)
order_2 = create_order(
    "ORD-1002", customers[1], products[1], products[2],
    shipping="express", priority=True,
)
order_3 = create_order(
    "ORD-1003", customers[2], products[3], products[4], products[5],
    discount=10,
)
order_4 = create_order(
    "ORD-1004", customers[3], products[6],
    gift_message="Happy Birthday!", delivery_instructions="Leave at reception",
)
order_5 = create_order(
    "ORD-1005", customers[4], products[7], products[0],
    shipping="standard", discount=5, campaign_code="SUMMER26",
)

orders = [order_1, order_2, order_3, order_4, order_5]

# --- Sanity-check helper ---
def print_order(order):
    """Print one order in a readable form, for dev-time sanity checks. It
    unpacks the nested customer dict and product list, since orders aren't
    flat records.
    """
    print(f"Order {order['order_id']}")
    print(f"  Customer: {order['customer']['name']} ({order['customer']['email']})")
    print(f"  Customer ID: {order['customer']['customer_id']}")

    product_list = ", ".join(
        f"{product['name']} ({product['price']:.2f} €)" for product in order["products"]
    )
    print(f"  Products: {product_list}")

    extra_info = {
        key: value for key, value in order.items()
        if key not in ("order_id", "customer", "products")
    }
    for key, value in extra_info.items():
        print(f"  {key}: {value}")
    print()


for order in orders:
    print_order(order)
