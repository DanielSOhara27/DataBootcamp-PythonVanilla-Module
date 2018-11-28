import csv
import os

csvPath = os.path.join("netflix_ratings.csv")
found = False

with open(csvPath, newline="") as netflix:
    csvReader = csv.reader(netflix, delimiter=",")
    csv_headers = next(csvReader)
    #csv_data = next(csvReader)

    searchVid = input("What is the exact name of the movie you are looking for? \n")

    for row in csvReader:
        if row[0].lower() == searchVid.lower():
            print(f"Title: {row[0]} \nRating: {row[1]}\nRating Score: {row[5]}")
            found = True
            break

    if not found:
        print(f"Sorry, we couldn't find the movie you searched")

