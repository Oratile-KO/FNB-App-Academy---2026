#Prompt user for input
firstname = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
age_in_months = age * 12
fav_num = float(input("Enter your favorite number: "))

#Display Student info
i = 1
while i <= 30:
    print("*", end="")
    i += 1

print(f"\nWelcome, {firstname} {surname}")

j = 1
while j <= 30:
    print("*", end="")
    j += 1

print(f"\nNAME: \t\t\t{firstname.upper()}")
print(f"NAME IN TITLE: \t\t{firstname.title()}")
print(f"AGE IN MONTHS: \t\t{age_in_months} months old")
print(f"FAVORITE NNUMBER: \t{round(fav_num, 2)}")
print(f"NAME DATA TYPE:\t\t {type(firstname)}")
print(f"SURNAME DATA TYPE:\t {type(firstname)}")
print(f"AGE DATA TYPE:\t\t {type(firstname)}")
print(f"FAVORITE NUMBER DATA TYPE:\t {type(firstname)}")


x = 1
while x <= 30:
    print("*", end="")
    x += 1
