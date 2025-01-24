import random
import hashlib

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nbr_letters = int(input("How many letters would you like in your password?\n"))
nbr_symbols = int(input(f"How many symbols would you like?\n"))
nbr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for char in range(1, nbr_letters + 1):
    password.append(random.choice(letters))

for char in range(1, nbr_symbols + 1):
    password.append(random.choice(symbols))

for char in range(1, nbr_numbers + 1):
    password.append(random.choice(numbers))

random.shuffle(password)

print(f"Your password is:\n{''.join(password)}")

hashed_pass = hashlib.sha256("".join(password).encode()).hexdigest()

print(f"The hash of your password is:\
    \n {hashed_pass}")






