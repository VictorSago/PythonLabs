
# ============================================================
# PART F - Applied challenge: Data cleanup
# ============================================================

# 1. At least twelve messy dictionaries representing products:
# inconsistent name casing/spacing, category, price and stock.
messy_products = [
    {"name": "  laptop", "category": "Electronics", "price": 999, "stock": 10},
    {"name": "MOUSE ", "category": "electronics", "price": 25, "stock": 150},
    {"name": "Keyboard", "category": "ELECTRONICS", "price": 45, "stock": 0},
    {"name": " monitor ", "category": "Electronics", "price": 250, "stock": 20},
    {"name": "desk chair", "category": "furniture", "price": 180, "stock": 5},
    {"name": "BOOKSHELF", "category": "Furniture", "price": 120, "stock": 0},
    {"name": "Coffee Mug", "category": "kitchen", "price": 8, "stock": 300},
    {"name": " blender", "category": "Kitchen", "price": 60, "stock": 15},
    {"name": "toaster ", "category": "KITCHEN", "price": 35, "stock": 0},
    {"name": "Notebook", "category": "Stationery", "price": 3, "stock": 500},
    {"name": "PEN SET", "category": "stationery", "price": 12, "stock": 80},
    {"name": "  desk lamp ", "category": "Furniture", "price": 40, "stock": 25},
]

# 2. A cleaned list where names/categories are normalized.
# Design: names are stripped + title-cased, categories are stripped +
# title-cased too, for consistent display and grouping later on.
cleaned_products = [
    {
        "name": product["name"].strip().title(),
        "category": product["category"].strip().title(),
        "price": product["price"],
        "stock": product["stock"],
    }
    for product in messy_products
]
print(cleaned_products)


# 3. A list of in-stock products.
products_in_stock = [product for product in cleaned_products if product["stock"] > 0]
print(products_in_stock)


# 4. A set of unique normalized categories.
unique_categories = {product["category"] for product in cleaned_products}
print(unique_categories)


# 5. A dictionary mapping product name to inventory value (price * stock).
inventory_value_by_product = {
    product["name"]: product["price"] * product["stock"] for product in cleaned_products
}
print(inventory_value_by_product)


# 6. Sort products by inventory value from highest to lowest.
# products_by_inventory_value = sorted(
#     cleaned_products,
#     key=lambda product: product["price"] * product["stock"],
#     reverse=True,
# )
products_by_inventory_value = sorted(
    cleaned_products,
    key=lambda product: inventory_value_by_product[product["name"]],
    reverse=True,
)
print(products_by_inventory_value)


# 7. Use enumerate to print a ranked report.
print("--- Inventory Value Ranking ---")
for rank, product in enumerate(products_by_inventory_value, start=1):
    inventory_value = inventory_value_by_product[product["name"]]
    print(f"{rank}. {product['name']} - {inventory_value}€")


# 8. Use zip to combine at least one pair of separate derived lists in
# a meaningful way.

products_sorted = sorted([product["name"] for product in cleaned_products])
values_sorted_by_name = [
    inventory_value_by_product[name] for name in sorted(inventory_value_by_product)
]
# Recombine the two derived lists with zip to show name/value pairs
for name, value in zip(products_sorted, values_sorted_by_name):
     print(f"{name}: {value}€")


# 9. A deliberately over-complicated comprehension, and a clearer
# alternative - explain why the clearer version wins.

# Over-complicated: nested nested comprehension crammed into one line,
# mixing normalization, filtering, AND a conditional expression all
# in a single unreadable statement.
over_complicated = {
    p["name"].strip().title(): (
        "High Value" if (p["price"] * p["stock"]) > 1000 else "Low Value"
    )
    for p in messy_products
    if p["stock"] > 0
    if p["price"] > 0
}
print(over_complicated)

# Clearer alternative: break the same logic into named, sequential
# steps - filter first, then classify, using the already-cleaned data
# instead of redoing the cleaning inline.
def classify_inventory_value(product):
    inventory_value = product["price"] * product["stock"]
    return "High Value" if inventory_value > 1000 else "Low Value"


in_stock_cleaned = [product for product in cleaned_products if product["stock"] > 0]
clearer_alternative = {
    product["name"]: classify_inventory_value(product) for product in in_stock_cleaned
}
print(clearer_alternative)

# Why the clearer version wins:
# The over-complicated version packs three separate concerns - name cleaning,
# stock/price filtering, and value classification - into one dense expression
# with two stacked if-clauses and a nested ternary. Understanding it means
# mentally unpacking all three at once. The clearer version names each step:
# a filter (in Ex 2), then a classification function with an obvious name,
# and finally, a comprehension step. In this way, each piece can be read,
# tested, and reused independently. It's a few more lines, but each line
# answers one question instead of one line answering all three.
