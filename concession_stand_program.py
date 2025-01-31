# Concession stand program

menu = {
    "pizza": 3,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "soda": 3.00,
    "lemonade": 4.25
}

# print(menu.items())
print("--------- MENU ---------")
for key, value in menu.items():
    print(f"{key:10}:  ${value:.2f}")
print("------------------------")

cart = []
while True:
    food = input("Select food from the menu or (q to Quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

total = 0
for food in cart:
    total += menu.get(food)
    # print(food, end=" ")

print("-------- Your Cart ........")
print(cart)
print()
print(f"TOTAL: ${total}")

