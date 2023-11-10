sandwich_orders = [
    'pastrami','chilli parotta', 'pastrami','chicken cheese', 'wraptor', 'pastrami'
    ]
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    sandwiches = sandwich_orders.pop()
    print(f"I'm working on your {sandwiches} sandwich.")
    finished_sandwiches.append(sandwiches)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")