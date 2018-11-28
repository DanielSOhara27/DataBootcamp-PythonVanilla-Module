candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Skittles", "Starburts", "M&Ms"]

allowance = int(input("How big is your allowance?"))

candyCart = list()

for cash in range(allowance):

    index = 0

    for candy in candyList:
       print(f"[{index}] {candy} \n")

       index +=1

    choice = int(input("Which candy do you want? "))
    candyCart.append(candyList[choice])


print(f'You have bougth: \n')

for x in candyCart:
    print(f"- {x}\n")