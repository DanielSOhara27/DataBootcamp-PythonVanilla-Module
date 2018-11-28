option = "y"
counter = 0

while option != "n":
    numbers = int(input("How many numbers should I print?"))
    for x in range(numbers):
        print(f"{counter}\n")
        counter += 1
    option = input("Do you want to print another range of numbers? (y)es or (n)o?")
