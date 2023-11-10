sandwich_orders = ['chilli parotta', 'chicken cheese', 'wraptor']
finished_sandwiches = []

while sandwich_orders:
    sandwiches = sandwich_orders.pop()
    print(f"I'm working on your {sandwiches} sandwich.")
    finished_sandwiches.append(sandwiches)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")