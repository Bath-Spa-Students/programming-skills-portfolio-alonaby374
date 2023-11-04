# Homogeneous List / Python Supports Hetrogeneous List other than C, Java

names=["Alon","Akku","Johan"]
print(names)


# Hetrogeneous List
Student=["Alon","123","3.89"]
print(Student)


# Repitition Operator * To repeat data
numbers=[1,2,3,4]
new_numbers=numbers * 2
print(new_numbers)


# Positive Indexing
numbers=[5,6,7,8,3,4]
print(numbers[-3])


# Negative Indexing starts from -1 , bcz 0 is a non-negative integer
numbers=[5,6,7,8,3,4]
print(numbers[-3])


# Lens function
numbers=[5,6,7,8,3,4]
print("number of elements in a list:" ,len(numbers))


# Mutability (Chageable)

numbers=[5,6,7,8,3,4]
numbers[0]=1
numbers[1]=9
print(numbers) 


# Concatenation

List_1=[2,3,4,5,6]
List_2=[9,8,7,6,5]

List_3=[List_1 + List_2]
print(List_3)


# List Slicing - to use one part of list

new_list=[1,2,3,10,15,6,7]
result=new_list[0:3]
print(result)


# find elements in list -if operator

new_list1=[1,2,3,4,5,6,7,8,9]
if 10 in new_list1:
    print("Found")
else:
    print("Not Found")


# (Not in) operator

new_list2=[1,2,3,4,5,6,7,8,9]
if 20 not in new_list2:
    print("Yes")
else:
    print("No")


# Built in methods - append

New_list3=[4,5,6,6,7]
New_list3.append(100)
print(New_list3)


# Built in methods - index

New_list4=[4,5,6,6,7]
print(New_list4.index(7))


# Built in methods - sort

New_list5=[4,5,6,3,1]
New_list5.sort()
print(New_list5)


# Built in methods - reverse

New_list6=[4,7,6,3,1]
New_list6.reverse()
print(New_list6)


# Built in methods - remove

New_list7=[4,7,6,3,1]
New_list7.remove(6)
print(New_list7)


# min max number
New_list8=[4,7,6,3,1]
print(max(New_list8))
print(min(New_list8))