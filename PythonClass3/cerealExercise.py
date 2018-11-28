import csv
import os

csvPath = os.path.join("cereal.csv")
csvPathBonus = os.path.join("cereal_bonus.csv")

with open(csvPath, newline="") as cereal:
    csvReader = csv.reader(cereal, delimiter=",")
    csvHeaders = next(csvReader)
    print(f"Header: {csvHeaders[7]}")

    cerealList = list()

    for cerealRow in csvReader:
        if (float(cerealRow[7]) >= 5):
            cerealList.append(cerealRow)
            print(cerealRow)

    print(f"I found {len(cerealList)} with 5 or more grams")
    for row in cerealList:
        print(f"Cereal Name: {row[0]} and len: {len(row)}")