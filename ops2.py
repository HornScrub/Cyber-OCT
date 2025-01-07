# Objectives
# Create if statements using these logical conditionals below.
# Each statement should print information to the screen depending on if the condition is met.

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are met or and else when no condition is met.

a = 8
b = 49
c = 9.99

if a != b:
    print("a is not equal to b")

if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else:
    print("a is equal to b")

if a >= c:
    print("a is greater than or equal to c")

if a > 0 and a < 10:
    print("a is between 0 and 10")

if b < 0 or b > 10:
    print("b is not between 0 and 10")

if a > 1:
    print("a is greater than 1")
    if a > 2:
        print("a is greater than 2")
        if a > 3:
            print("a is greater than 3")

if not a == b:
    print("a is not equal to b")

if a != b:
    print("a is not equal to b")

# Stretch Goals (Optional Objectives)
# Pursue stretch goals if you are a more advanced user or have remaining lab time.

# Create an if statement with two conditions by using "and" between conditions.

# Create an if statement with two conditions by using "or" between conditions.

# Create a nested if statement.

# Hint:  a = int(input("Enter a number "))

