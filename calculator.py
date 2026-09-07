#Prompt user for input
num_1 = float(input("Inserts your first number: ").strip())
num_2 = float( input("Inserts your second number: ").strip())

#Handle input of 0
while num_2 == 0:
    num_2 =float(input("Cannot divide by 0, please enter another number: "))

#Display calculated output
i = 1
while i <= 30:
    print("*", end="")
    i += 1

print("\nMulti-Function Calculator")

j = 1
while j <= 30:
    print("*", end="")
    j += 1

print(f"\nADDITION:\t {round(num_1 + num_2, 2)}")
print(f"SUBTRACTION:\t {round(num_1 - num_2, 2)}")
print(f"MULTIPLICATION:\t {round(num_1 * num_2, 2)}")
print(f"DIVISION:\t {round(num_1 / num_2, 2)}")
print(f"FLOOR DIVISION:\t {num_1 // num_2}")
print(f"MODULUS: {round(num_1 % num_2, 2)}")

x = 1
while x <= 30:
    print("*", end="")
    x += 1

