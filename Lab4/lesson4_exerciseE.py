
# ============================================================
# Part E - Decomposition
# ============================================================

# 1. Temperature report using separate functions for conversion,
# classification, and formatting.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def classify_temperature(celsius):
    if celsius < 10:
        return "cold"
    elif celsius < 25:
        return "warm"
    else:
        return "hot"


def format_temperature_report(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    category = classify_temperature(celsius)
    return f"{celsius}°C ({fahrenheit}°F) - {category}"


# print(format_temperature_report(5))
# print(format_temperature_report(18))
# print(format_temperature_report(30))

# 2. Small order calculation using separate functions for subtotal,
# discount and final total.
def calculate_subtotal(price, quantity):
    return price * quantity


def calculate_discount_amount(subtotal, discount_percent):
    return subtotal * discount_percent / 100


def calculate_difference(subtotal, discount_amount):
    return subtotal - discount_amount


def calculate_final_total(price, quantity=1, discount_percent=0):
    subtotal = calculate_subtotal(price, quantity)
    discount_amount = calculate_discount_amount(subtotal, discount_percent)
    return calculate_difference(subtotal, discount_amount)


# print(calculate_final_total(20, 3, 10))

# 3. Refactor one earlier exercise that contains repeated code into
# at least three functions.
#
# calculate_final_total (exercise 2, above) already calls calculate_subtotal() 
# and calculate_discount_amount(), so adding the function that does the final
# subtraction causes it to call three functions, and no calculation logic is 
# written directly inside it anymore - it's purely a coordinator.


# 4. A main-like section at the bottom of the file that calls the
# functions above in a clear sequence.
def main():
    print("--- Temperature Report ---")
    print(format_temperature_report(5))
    print(format_temperature_report(18))
    print(format_temperature_report(30))

    print("\n--- Order Calculation ---")
    final_total = calculate_final_total(20, 3, 10)
    print("Final total:", final_total)

    print("\n--- Refactored Price Calculation ---")
    price_result = calculate_final_total(10, 3, 20)
    print("Price after discount:", price_result)


main()
