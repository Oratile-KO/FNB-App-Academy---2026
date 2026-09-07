#Prompt user for input
name = input("Enter your name: ").strip()
surname = input("Enter your surname: ").strip()
bio_message = input("Enter a short bio message: ").strip()
username = name[0] +  surname

i = 1
while i <= 30:
    print("*", end="")
    i += 1

print(f"\nString Formatter")

j = 1
while j <= 30:
    print("*", end="")
    j += 1

print(f"\nNAME:\t\t {name.title()} {surname.title()}")
print(f"USERNAME:\t\t {username}")
print(f"BIO:\t\t {bio_message}")
print(f"CHARACTERS IN BIO: {len(bio_message)}")
print(f"REPLACED BIO: {bio_message.replace("I am", "I'm")}")

x = 1
while x <= 30:
    print("*", end="")
    x += 1