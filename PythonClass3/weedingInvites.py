guests = list()

for x in range(5):
    guests.append(input("Who do you want to invite? "))

guests2 = [guests.lower() for guests in guests]
guests3 = [guests2.title() for guests2 in guests2]
invitations = [f"Dear {name}, please come to the wedding this Sunday!" for name in guests3]

for invitation in invitations:
    print(invitation)

