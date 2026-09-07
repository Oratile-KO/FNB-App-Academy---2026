#Prompt user for input
password = input("Enter your password: ").strip()
first_character = password[0]
last_character = password[-1]

print(f"Password Hint: It starts with {first_character} and ends with {last_character}")
