print("Welcome to TechDam food restaurant!")

foods = []
prices = []
cart_total = 0
while True:
    food = input("Enter a food to buy (q to quit): ").lower()
    if food == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("------------ Your Cart -----------")
for food in foods:
    print(food, end=" ")

for price in prices:
    cart_total += price

print()
print(f"Your total is ${cart_total}")