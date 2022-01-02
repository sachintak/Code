# List are container to store a set of vales of any data type 
# Sqaure brackets [] are use to create the list 
# Items are seperated by the comma "," in these list 
# We can store a list into the list that means any kind of data type can be stored in list

a = "Hey Sachin"
b = 16 
c = True

myList = [a, b, c, 'June', 16, 1998]
print(myList)
print(type(myList))

print(myList[0]) # Print 0th index element from list
print(myList[1])
print(myList[-1])

print(myList[0:3]) # Slicing of list

print(myList[0:20]) # It will print the whole list beacuse index 20th not present so it will 
# print till the end

print("list 2:",myList[0:]) 