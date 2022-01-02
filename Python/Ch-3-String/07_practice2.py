date = input("Enter the Date: ")
name = input("Enter your name: ")

template = ''' Dear <|name|>
You are selected
<|date|>
'''
print(template.replace('<|name|>',name).replace('<|date|>',date))

