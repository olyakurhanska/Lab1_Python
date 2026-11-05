
products = [
    ("Хліб", 7, 32),
    ("Молоко", 4, 48),
    ("Сир", 3, 115),
    ("Яблука", 9, 27)
]

def show_product(product):
    name, quantity, price = product
    print(name, "- кількість:", quantity, "ціна:", price, "грн")

for product in products:
    show_product(product)
    
def total_cost(products):
    total = 0
    for name, quantity, price in products:
        total += quantity * price
    return total

print("Загальна вартість товарів:", total_cost(products), "грн")

print("\nПеревірка незмінності кортежу:")

try:
    products[0][1] = 10
except TypeError:
    print("Елемент кортежу змінити не можна")

product_info = ("Ноутбук", [12, 15, 18])

print("\nКортеж зі списком:", product_info)

product_info[1].append(20)

print("Після зміни списку:", product_info)
