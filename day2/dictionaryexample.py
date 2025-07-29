# Dictionary of product details
products = {
    201: {"prdname": "Laptop", "qty": 15},
    202: {"prdname": "Mouse", "qty": 50},
    203: {"prdname": "Keyboard", "qty": 30}
}

# 1. Retrieve a product by key
product_202 = products.get(202)

# 2. Add a new product
products[204] = {"prdname": "Monitor", "qty": 20}

# 3. Update an existing product's quantity
products[203]["qty"] = 35

# 4. Remove a specific product using pop()
removed_product = products.pop(202)

# 5. Remove the last added product using popitem()
last_removed = products.popitem()

# 6. Extract keys, values, and key-value pairs
all_keys = products.keys()
all_values = products.values()
all_items = products.items()

# 7. Clear the dictionary
products.clear()

# ----------- OUTPUT ------------
print("Details of product 202 before removal:", product_202)
print("Removed product 202:", removed_product)
print("Last removed product (popitem):", last_removed)
print("All product IDs (keys):", all_keys)
print("All product details (values):", all_values)
print("All product entries (items):", all_items)
print("Dictionary after clear():", products)
