# program to understand bytearray type array

# create a list of byte numbers
elements =[10,20,0,40,15]

# convert the list into bytearray type array
x = bytearray(elements)

# modify the first two elements of x
x[0] = 88
x[1] = 99

# retrieve elements from x using for loop and display
for i in x: print(i)