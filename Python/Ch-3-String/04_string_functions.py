
myStr = "abcdefghijklmnopqrstuvwxyz cdef"

print(len(myStr)) # len() - this function will print the length of the string 

print(myStr.endswith("yz")) # string.endswith() - this function will print the output as boolean, that weather string ends with give character or not

print(myStr.startswith("abc")) # this function will determine with string starts with this or not 

print(myStr.count('a')) # it will count the occurance of specific character/string 
print(myStr.count('ab'))
print(myStr.count('cdef'))
print(myStr.count('abd'))

myStr2 = "Sachin my name is Sachin"

print(myStr2.capitalize()) # It will capatilize the first character of string 

print(myStr2.find('s')) # it will find the character/words in the string and return first occurance index number

# str.replace("old word","new word") - it will replace the word in whole string
print(myStr2.replace('Sachin','Muskan'))