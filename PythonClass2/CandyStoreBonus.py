candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Skittles", "Starburts", "M&Ms"]

allowance = "y"

candyCart = list()

while allowance != "n":

    index = 0

    for candy in candyList:
       print(f"[{index}] {candy} \n")

       index +=1

    choice = int(input("Which candy do you want? "))
    candyCart.append(candyList[choice])

    allowance = input("Do you want more candy? (y)es or (n)o ")

print(f'You have bought: \n')

for x in candyCart:
    print(f"- {x}\n")