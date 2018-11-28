fish = "halibut"

# Loop through each letter in the string
# and push to an array

letters = []
for letter in fish:
    letters.append(letter)

print(letters)

# List comprehensions provide concise syntax for creating lists
# This are lists that have a for loop inside themselves
letters = [letter for letter in fish]

print(letters)

# We can manipulate each element as we go
capital_letters = []
for letter in fish:
    capital_letters.append(letter.upper())

print(capital_letters)

# List Comprehension for the above
capital_letters = [letter.upper() for letter in fish]

print(capital_letters)

# We can also add conditional logic (if statements) to a list comprehension
july_temperature = [87, 85, 92, 70, 106]
hot_days = []
for tempereature in july_temperature:
    if tempereature > 90:
        hot_days .append(tempereature)
print(hot_days)

# List comprehension with conditional
hot_days = [temperature for temperature in july_temperature if tempereature > 90]
print(hot_days)