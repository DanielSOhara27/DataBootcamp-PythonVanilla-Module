option = "y"

while option != "n":
    numbers = int(input("How many numbers should I print?"))
    for x in range(numbers):
        print(f"{x}\n")
    option = input("Do you want to print another range of numbers? (y)es or (n)o?")
