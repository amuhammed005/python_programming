principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than or equal to zero")
    else:
        break;

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than or equal to zero")
    else:
        break;

while True:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")
    else:
        break;

# print(f"Principle: {principle}, Rate: {rate}, Time: {time}")

total_amount = principle * pow(1 + (rate / 100), time)
print(f"Your balance after {time} year/s is: ${total_amount:.2f}")