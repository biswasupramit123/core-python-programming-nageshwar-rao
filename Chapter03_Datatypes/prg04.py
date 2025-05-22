# program to understand bytes type array

# create a list of byte numbers
elements = [10,20,0,40,15]

# convert the list into bytes type array
x = bytes(elements)
print("The byte array is: ", x)

for i in x: print(i)
# convert the byte array into list