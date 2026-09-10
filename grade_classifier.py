#Prompt user for input
name = input("Enter your name: ").strip()
math_mark = float(input("Enter your Math mark: ").strip())
physics_mark = float(input("Enter your Physics mark: ").strip())
setswana_mark = float(input("Enter your Setswana mark: ").strip())

#Calculate the average
average = (math_mark + physics_mark + setswana_mark) / 3

#Assign a letter grade: A (80+), B (70-79), C (60-69), D (50-59), F (below 50) using if/elif/else
if average > 79:
    grade = 'A'
elif average > 69:
    grade = 'B'
elif average > 59:
    grade = 'c'
elif average > 49:
    grade = 'D'
else: 
    grade = 'F'

#Assign Pass status if the average is 50 or above, Fail otherwise
if average >= 50:
    status = "Pass"
else:
    status = "Fail"

#Flag any individual subject mark below 40 as ‘needs intervention’
needs_intervention = [] #Create a list to store the subjects that need intervention

#Add subject to the list if markk if below 40
if math_mark < 40:
    needs_intervention.append("Math")
if physics_mark < 40: 
    needs_intervention.append("Physics")
if setswana_mark < 40:
    needs_intervention.append("Setswana")

#print report
# print(*needs_intervention, sep=', ')

i = 1
while i <= 30:
    print("*", end="")
    i += 1

print("\n\tREPORT CARD")

j = 1
while j <= 30:
    print("*", end="")
    j += 1

print(f"\nNAME: \t\t{name}")
print(f"MATH MARK: \t\t{math_mark}")
print(f"PHYSICS MARK: \t\t{physics_mark}")
print(f"SETSWANA MMARK: \t{setswana_mark}")
print(f"AVERAGE: \t\t{average}")
print(f"GRADE: \t\t{grade}")
print(f"STATUS: \t\t{status}")
print(*needs_intervention[:-1], sep=", ", end=", ")
print(needs_intervention[-1], "need intervention")

x = 1
while x <= 30:
    print("*", end="")
    x += 1