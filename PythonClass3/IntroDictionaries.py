myDictionary = dict()

myDictionary.update({'name': 'Daniel', 'age': 28, 'hobbies': {'videogames', 'reading', 'movies'}, 'wakeup': {'Mon': '8:00', 'Tue': '9:00', 'Wed': '10:00'}})

print(f"Hi! My name is {myDictionary['name']} and I have {len(myDictionary['hobbies'])} and Mondays I wake up at {(myDictionary['wakeup'])['Mon']} ")