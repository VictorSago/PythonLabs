
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
    {"name": "Laptop", "price": 750.00, "category": "Electronics"},
    {"name": "Desk", "price": 150.00, "category": "Home"}
]

customers = [
    {"name": "Anna Andersson", "email": "anna.andersson@example.com", "customer_id": "C001"},
    {"name": "David Kim", "email": "david.kim@example.com", "customer_id": "C002"},
    {"name": "Sara Nilsson", "email": "sara.nilsson@example.com", "customer_id": "C003"},
    {"name": "Leo Martins", "email": "leo.martins@example.com", "customer_id": "C004"},
    {"name": "Mia Fischer", "email": "mia.fischer@example.com", "customer_id": "C005"},
    {"name": "Arthur Dent", "email": "arthur.dent@example.com", "customer_id": "C006"}
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


# --- Part 3 - Variable number of products ---
def calculate_subtotal(*prices):
    """Calculate the subtotal for a variable number of product prices.

    Works the same way whether called with one price, several, or none
    at all (an empty call simply returns 0).
    """
    return sum(prices)


# --- Alternative - calculate_subtotal without sum() ---
def calculate_subtotal_the_hard_way(*prices):
    """Same result as calculate_subtotal(), but built with a manual loop
    instead of sum() - kept only to show what the "hard way" looks like.
    """
    total = 0
    for price in prices:
        total += price
    return total


single_price_subtotal = calculate_subtotal(199)
multiple_prices_subtotal = calculate_subtotal(199, 349, 99, 129)
no_prices_subtotal = calculate_subtotal()
print("Subtotal for one price:", single_price_subtotal)
print("Subtotal for several prices:", multiple_prices_subtotal)
print("Subtotal with no prices supplied:", no_prices_subtotal)


# --- Part 4 - Order configuration ---
def configure_order_settings(**settings):
    """Process a set of optional order settings, supplied as keyword
    arguments, and return them as a dict.
    """
    return {key: value for key, value in settings.items() if value is not None}


# settings_1 = configure_order_settings(shipping="express", priority=True, discount=10)
# settings_2 = configure_order_settings(shipping="standard", gift_message="Happy birthday!")
# settings_3 = configure_order_settings(shipping="standard", discount=None, priority=False)
# print(settings_1)
# print(settings_2)
# print(settings_3)


# --- Part 5 - Unpacking existing data ---

# Positional unpacking (*) - existing lists/tuples used as positional args

# Example A: a tuple of prices, already collected elsewhere, unpacked
# straight into calculate_subtotal() instead of retyped one by one.
weekend_sale_prices = (199, 349, 99, 129)
weekend_sale_subtotal = calculate_subtotal(*weekend_sale_prices)

# Example B: a list of products, already selected elsewhere, unpacked
# into create_order()'s *order_products.
selected_products = [products[0], products[2], products[5]]
order_6 = create_order("ORD-1006", customers[0], *selected_products, shipping="standard")
orders.append(order_6)

print("Weekend sale subtotal:", weekend_sale_subtotal)
print_order(order_6)


# Dictionary unpacking (**) - existing dicts used as keyword arguments

# Example A: this dict contains everything configure_order_settings() needs.
autumn_campaign_settings = {
    "shipping": "standard",
    "discount": 15,
    "gift_message": "Thanks for shopping with us!",
}
autumn_settings = configure_order_settings(**autumn_campaign_settings)

# Example B: an existing options dict unpacked directly into
# create_order()'s **order_options, alongside its positional arguments.
express_options = {"shipping": "express", "priority": True}
order_7 = create_order("ORD-1007", customers[3], products[1], **express_options)
orders.append(order_7)

print("Autumn campaign settings:", autumn_settings)
print_order(order_7)


# --- Part 6 - Flexible order summary ---
def order_summary(order_id, customer, *notes, **metadata):
    """Build a readable, multi-line order summary.

    order_id and customer are required; *notes accepts any number of messages
    or notes (including none at all), and **metadata accepts whatever extra
    information is relevant for a given order.
    """
    lines = [f"Order {order_id}", f"Customer: {customer}"]

    if notes:
        lines.append("Notes:")
        for note in notes:
            lines.append(f"  - {note}")

    if metadata:
        lines.append("Metadata:")
        for key, value in metadata.items():
            lines.append(f"  {key}: {value}")

    return "\n".join(lines)


summary_1 = order_summary(
    "ORD-1042",
    "Anna Andersson",
    "Express delivery",
    "Leave at reception",
    priority=True,
    campaign="SUMMER26",
)

# With a different number of notes and metadata fields
summary_2 = order_summary(
    "ORD-1003",
    customers[2]["name"],
    "Gift wrap requested",
    discount=10,
)

# No notes and no metadata at all - still a valid, readable summary.
summary_3 = order_summary("ORD-1001", customers[0]["name"])

# print(summary_1)
# print(summary_2)
# print(summary_3)


# --- Part 7 - Scope and order statistics ---
STORE_NAME = "PixelMart"
TAX_RATE = 0.25
total_orders_processed = 0

# Reading a global variable from inside a function - this never needs
# the `global` keyword, only reassigning a global does.
def store_welcome_message():
    return f"Welcome to {STORE_NAME}!"


# Creating a local variable with the same name as a global - this
# shadows the global inside this function only, and does not modify it.
def preview_store_name(candidate_name):
    STORE_NAME = candidate_name
    return f"Preview: {STORE_NAME}"


print(store_welcome_message())
print(preview_store_name("Test Store"))
print("Global STORE_NAME is still:", STORE_NAME)


# Attempting to assign to a global numeric variable inside a function, without
# the `global` keyword. Because it assigns to total_orders_processed, Python
# treats it as a local variable for the *entire* function body - so reading it
# on the right-hand side, before any local assignment has actually happened,
# raises an UnboundLocalError rather than reading the global.
def broken_increment_orders_processed():
    total_orders_processed += 1
    return total_orders_processed


# This will break the script
# broken_increment_orders_processed()


# The preferred design: instead of using `global` to mutate the global counter,
# the function takes the current count as an argument and returns the new value.
# The caller updates the global variable explicitly. This keeps the function
# pure and independently testable, and makes the fact that the global variable
# changes visible at the call, rather than hidden inside the function.
def increment_orders_processed(current_count):
    return current_count + 1


total_orders_processed = increment_orders_processed(total_orders_processed)
total_orders_processed = increment_orders_processed(total_orders_processed)
print("Total orders processed:", total_orders_processed)

# Enclosing scope: a nested function can read a variable from its enclosing
# function's scope directly, without it being passed in as an argument.
def outer_func():
    order_id = "ORD-2001"

    def inner_func():
        print(f"Processing order: {order_id}")

    inner_func()


outer_func()


# --- Part 8 - Order processing ---
SHIPPING_COSTS = {"standard": 4.99, "express": 12.99}


def process_order(order_id, customer, *order_products, **order_settings):
    """Process an order and return its subtotal, discount, shipping cost,
    tax and final total.

    order_id and customer are always required and single-valued, so they are
    normal named parameters. The products in an order can be any number, so
    they are collected with *order_products. Which settings apply differs from
    order to order and none of them are required, so they are collected with
    **order_settings instead of being listed. Using *args or **kwargs for
    order_id/customer, on the other hand, would only make the function harder
    to call correctly for no real benefit.
    """
    subtotal = calculate_subtotal(*(product["price"] for product in order_products))

    discount_percentage = order_settings.get("discount", 0)
    discount_amount = subtotal * discount_percentage / 100

    shipping_method = order_settings.get("shipping", "standard")
    shipping_cost = SHIPPING_COSTS.get(shipping_method, SHIPPING_COSTS["standard"])

    taxable_amount = subtotal - discount_amount
    tax_amount = taxable_amount * TAX_RATE

    final_total = taxable_amount + shipping_cost + tax_amount

    return {
        "order_id": order_id,
        "customer": customer,
        "subtotal": round(subtotal, 2),
        "discount": round(discount_amount, 2),
        "shipping_cost": shipping_cost,
        "tax": round(tax_amount, 2),
        "final_total": round(final_total, 2)
    }


# A helper for printing processed orders
# A processed order is flat - customer is already a plain string and there's
# no nested product list, so print_order() doesn't apply here, and neither does
# order_summary(). This is a small, separate printer for the flatter shape.
def print_processed_order(processed_order):
    print(f"Order {processed_order['order_id']}")
    print(f"  Customer: {processed_order['customer']}")
    for key, value in processed_order.items():
        if key in ("order_id", "customer"):
            continue
        if isinstance(value, float):
            print(f"  {key}: {value:.2f} €")
        else:
            print(f"  {key}: {value}")
    print()


# --- Part 9 - Different order types ---
# The orders already created in Parts 2 and 5 already cover every
# required category below, so no new orders need to be invented just
# for this part:
#   - one product:            order_1, order_4, order_7
#   - several products:       order_2, order_3, order_6
#   - no discount:             order_1, order_2, order_4, order_6, order_7
#   - with a discount:         order_3, order_5
#   - express order:           order_2, order_7
#   - additional metadata:     order_4 (gift_message, delivery_instructions),
#                               order_5 (campaign_code)
processed_orders = []

for order in orders:
    order_options = {
        key: value for key, value in order.items()
        if key not in ("order_id", "customer", "products")
    }
    processed_order = process_order(
        order["order_id"], order["customer"]["name"], *order["products"], **order_options
    )
    processed_orders.append(processed_order)
    print_processed_order(processed_order)


# --- Final Challenge - Daily Order Report ---
def create_report(title, *sections, **metadata):
    """Build a structured report.

    title is required; *sections accepts any number of report sections, each
    expected as a (heading, content_lines) pair, and **metadata accepts
    optional extra information without needing to be declared ahead of time.
    Returns a structured dict rather than printed text.
    """
    return {
        "title": title,
        "sections": list(sections),
        "metadata": metadata
    }


def report_to_string(report):
    """Convert a structured report into a readable multi-line string."""
    lines = [report["title"], "=" * len(report["title"])]

    for heading, content_lines in report["sections"]:
        lines.append("")
        lines.append(heading)
        lines.append("-" * len(heading))
        lines.extend(content_lines)

    if report["metadata"]:
        lines.append("")
        lines.append("Metadata")
        lines.append("-" * len("Metadata"))
        for key, value in report["metadata"].items():
            lines.append(f"{key}: {value}")

    return "\n".join(lines)


# Required statistics
number_of_orders = len(processed_orders)
total_revenue = round(sum(order["final_total"] for order in processed_orders), 2)
average_order_value = round(total_revenue / number_of_orders, 2)
# Finding max without using the built-in was demonstrated in previous labs
largest_order = max(processed_orders, key=lambda order: order["final_total"])
smallest_order = min(processed_orders, key=lambda order: order["final_total"])

# Two additional statistics
total_discount_given = round(sum(order["discount"] for order in processed_orders), 2)
total_tax_collected = round(sum(order["tax"] for order in processed_orders), 2)

summary_section = (
    "Summary",
    [
        f"Number of orders: {number_of_orders}",
        f"Total revenue: {total_revenue:.2f} €",
        f"Average order value: {average_order_value:.2f} €",
        f"Total discount given: {total_discount_given:.2f} €",
        f"Total tax collected: {total_tax_collected:.2f} €",
    ]
)

largest_smallest_section = (
    "Largest & smallest orders",
    [
        f"Largest: {largest_order['order_id']} ({largest_order['customer']}) - "
        f"{largest_order['final_total']:.2f} €",
        f"Smallest: {smallest_order['order_id']} ({smallest_order['customer']}) - "
        f"{smallest_order['final_total']:.2f} €",
    ]
)

daily_report = create_report(
    "Daily Order Report",
    summary_section,
    largest_smallest_section,
    generated_by="Order Management System",
    department="Sales",
    date="2026-09-18",
    version="1.0",
)

print(report_to_string(daily_report))


# --- Design Challenge ---
#
# Example 1: create_order(order_id, customer, *order_products, **order_options)
# Why: order_id and customer are always required and always exactly one value
#   each, so they are normal named parameters. The number of products in an
#   order varies, so they are collected in *order_products. Which settings
#   apply differs per order, so those are collected with **order_options.
# Alternative considered: requiring products as an explicit list parameter,
#   e.g. create_order(order_id, customer, products_list, **order_options).
# Why the final version is clearer: the caller can list products directly at
#   the call site instead of having to build a list first.
#
# Example 2: calculate_subtotal(*prices)
# Why: the function needs to work with any number of prices, including zero, 
#   without needing a different function per product count.
# Alternative considered: a single prices parameter expecting a list or
#   tuple, e.g. calculate_subtotal(prices_list).
# Why the final version is clearer: calling it with a handful of prices reads
#   naturally, instead of forcing the caller to wrap them in a list or tuple
#   first, even for a single price. With a list-based design, calling 
#   calculate_subtotal(199) instead of calculate_subtotal([199]) would
#   immediately fail with TypeError: 'int' object is not iterable, since sum()
#   cannot work with a bare number - the caller would have to remember, for
#   every call, that even a single price needs wrapping. *prices accepts both
#   a single value and several without the caller needing to think about it.
#
# Example 3: configure_order_settings(**settings)
# Why: the set of possible settings is open-ended and varies between orders.
# Alternative considered: declaring every known setting as its own optional 
#   parameter, e.g. configure_order_settings(shipping=None, discount=None,
#   priority=None, gift_message=None, ...).
# Why the final version is clearer: a fixed list of optional parameters forces
#   the function's own signature to grow every time a new kind of setting is
#   needed, and it gets long and hard to scan. **kwargs supports a brand-new
#   setting - say, a future "insurance" option - the moment a caller starts
#   passing it, with zero changes to configure_order_settings itself, whereas
#   the explicit-parameter version would require editing the function's
#   definition just to accept one more option.
#
# Where *args/**kwargs would make things LESS clear:
# process_order(order_id, customer, *order_products, **order_settings)
#   deliberately keeps order_id and customer as normal parameters rather than
#   folding them into **order_settings alongside the optional settings. If
#   they were just two more keys in a general kwargs dict, Python would no
#   longer enforce that they're actually supplied - forgetting order_id would
#   fail with a KeyError, instead of an immediate, clear "missing required
#   argument" error at the call site. Keeping them explicit also makes it
#   obvious, just from the function signature, which two pieces of information
#   every call actually requires versus what's merely optional.
