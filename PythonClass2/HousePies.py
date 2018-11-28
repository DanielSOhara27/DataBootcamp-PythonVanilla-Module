pieList = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry", "Buko", "Burek", "Tamale", "Steak"]
pieOrder = list()
flag = "y"

while flag != "n":
    print(f"Welcome to the House of Pies! Here are oure Pies:\n\n{' _ '*30}\n(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, (9) Tamale, (10) Steak\n")

    choice = int(input("Which pie do you want? "))

    print(f"Great! We'll have that {pieList[choice-1]} right out for you.")
    pieOrder.append(pieList[choice - 1])

    flag = input("\nDo you want to order another pie? (y)es or (n)o  ")

for pie in pieList:
    print(f"{pieOrder.count(pie)} {pie}")
print(f"{'-'*30}\nTotal Pies: {len(pieOrder)}")