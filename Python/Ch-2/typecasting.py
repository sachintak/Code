a=7
b="7"
print(a==b) # It will be false beacuse 'b' is string and 'a' is int 

c=int(b)  # b i.e. string is converted int 
print(a==c)
print(b==c)

print(type(c))
print(type(b))
print(type(a))

# ------------------

d="y"
e=int(d)
print("type conversion",e)
