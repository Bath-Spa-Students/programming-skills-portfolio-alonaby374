guests = ['Shah Rukh Khan','Tom Cruise','Leonardo DiCaprio']

name = guests[0]
print(f"{name}, please come have dinner with me.")

name = guests[1]
print(f"{name}, please come have dinner with me.")

name = guests[2]
print(f"{name}, please come have dinner with me.")

name = guests[1]
print(f"\nSorry, {name} can't make it to dinner.")

del(guests[1])
guests.insert(1, 'Johnny Depp')

name = guests[0]
print(f"{name}, please come have dinner with me.")

name = guests[1]
print(f"{name}, please come have dinner with me.")

name = guests[2]
print(f"{name}, please come have dinner with me.")

print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print(f"Sorry, {name} there's no room at the table.")

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

del(guests[0])
del(guests[0])

print(guests)