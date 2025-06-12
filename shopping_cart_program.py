print("Welcome to TechDam food restaurant!")

foods = []

prices = []
cart_total = 0
while True:
    food = input("Enter a food to buy (q to quit): ").strip().lower()
    if food == "q":
        break

    while True:
        price = input(f"Enter the price of {food}: $").strip()
        try:
            price = float(price);
            if price  < 0:
                print("Price can not be negative. Please enter a valid price")
            else:
                break
        except ValueError:
            print("Invalid input. Enter a valid number")
    
    foods.append(food)
    prices.append(price)

print("\n------------ Your Cart -----------")
for food, price in zip(foods, prices):
    print(f"{food.capitalize()}:  ${price:.2f}")

cart_total = sum(prices)
print(f"\nYour total is ${cart_total:.2f}")