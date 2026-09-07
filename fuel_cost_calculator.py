#Prompt user for input
kilometers = float(input("How many kilometeres do you wwant to travel: ").strip())
price_per_litre = float(input("What is the current fuel price per litre: ").strip())
liters_needed = kilometers / 10

total_cost = round(liters_needed * price_per_litre, 2)

print(f"The total cost for the trip is R{total_cost}")
