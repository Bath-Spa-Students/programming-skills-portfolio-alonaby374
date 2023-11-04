pets = []

pet = {
    'animal type': 'Dog',
    'name': 'Leo',
    'owner': 'Alon',
}
pets.append(pet)

pet = {
    'animal type': 'Cat',
    'name': 'Simba',
    'owner': 'Asvin',
}
pets.append(pet)

pet = {
    'animal type': 'Rabbit',
    'name': 'Flopsy',
    'owner': 'Aby',
}
pets.append(pet)

for pet in pets:
    print(f"\nHere's what I know about {pet['name']}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")