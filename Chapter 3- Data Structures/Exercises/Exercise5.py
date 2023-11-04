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

