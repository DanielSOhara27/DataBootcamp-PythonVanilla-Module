import csv
import os

csvPath = os.path.join("WWE-Data-2016.csv")
keepGoing = 'y'

def getPercentages(wrestlerData):
    wins = float(wrestlerData[1])
    loss = float(wrestlerData[2])
    draw = float(wrestlerData[3])
    total = wins + loss + draw
    winRatio = (wins / total) * 100
    lossRatio = (loss / total) * 100
    drawRatio = (draw / total) * 100

    print(f"- {wrestlerData[0]}\nWins %: {winRatio}\nLoss %: {lossRatio}\nDraw %: {drawRatio}")

def checkWrestlerData(filePath):
    with open(filePath, newline="") as wresterFile:
        csvReader = csv.reader(wresterFile, delimiter=",")
        csvHeaders = next(csvReader)

        for wrestler in csvReader:
            print(f"{wrestler[0]}")
        nameToCheck = input("What wrestler do you want to look for? ")

        wresterFile.seek(1)

        for wrestler in csvReader:
            # print(f"{wrestler[0].lower()} vs u:{nameToCheck.lower()}")
            if (wrestler[0].lower() == nameToCheck.lower()):
                getPercentages(wrestler)

while keepGoing.lower() != 'n':
    checkWrestlerData(csvPath)
    keepGoing = input("Do you want to look for another wrestler? (y)es or (n)o ")