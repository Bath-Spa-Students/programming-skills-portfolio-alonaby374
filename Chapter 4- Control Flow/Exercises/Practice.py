'''a=0
age=int(input("Enter Age: "))
if age >= 18 :
    a=("Adult")
else :
    a=("Minor")
print("Your Status: "+str(a))'''


# Nested Decision Structure
age = int(input("Enter your Age: "))
income = int(input("Enter your annual income: "))

if age >= 18:
    if income >= 25000:
        print("You Qualify for the Credit Card.")
    else:
        print("Sorry, your income is below the Minimum Requirement.")
else:
    print("You must be at least 18 Years Old to apply for the Credit Card.")
