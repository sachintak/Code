l1 = [1,2,3,5,8,16,23,55,7]
# sachinTakList = [16,6,1998]
# print(stl) = print(sachinTakList)

myListOfNumbers = [1, 8, 7, 2, 21, 15]
print(myListOfNumbers)

myListOfNumbers.sort()
# a = myListOfNumbers.sort()
print(myListOfNumbers)

# .sort doesn't return anything it updates the list 
# print(a) # output will be none 

myListOfNumbers.reverse()  # Reverse the list
print(myListOfNumbers)

myListOfNumbers.append(9) # it will append 9 at the end of the list 
print(myListOfNumbers)  


# myListOfNumbers.insert(2,'Sachin')
# print(myListOfNumbers)
myListOfNumbers.insert(2,7)  # It will insert 7 at index 2
print(myListOfNumbers)

myListOfNumbers2 = [1,2,4,5,7,3]
print(myListOfNumbers2)
# myListOfNumbers2.pop() # it will delete the item from the end of the list 
# print(myListOfNumbers2)
# myListOfNumbers2.pop(2) # it will remove the value form index 2 
# print(myListOfNumbers2)

myListOfNumbers2.remove(3) # it will remove particular item from the list (it will remove 3)
print(myListOfNumbers2)
myListOfNumbers2.remove(2) # it will remove particular item from the list (it will remove 2)
print(myListOfNumbers2)

myl1 = [1,2,2,3,4,5,6,1,3]
myl1.remove(3) # If there is duplicate values in the list then it will remove only first occurance 
print(myl1)
