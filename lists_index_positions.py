# Python considers the first item in a list to be at position 0 and not position 1
# most programing languages are in this format the technical name for this is zero based

bicycles = ['trek','cannondale','redline','specialized']
print (bicycles[0])
print (bicycles[3])

# print (bicycles[4])
# note in the above call we addressed a element in our list that does not exist and would give an out of range error 
# pay attention as you design your programs to address this possible issue

# python also has a special syntax for accessing the last element in the list "[-1]" calling this address
# will always result in python returning the last item in the list
print (bicycles[-1])

# this special call extends to other addresses as well we can call out [-2],[-3] and so on, it will access an element
# further from the back of the list in this case the second and third from the last elements
print (bicycles[-2])
print (bicycles[-3])
