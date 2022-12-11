# most lists you create will be dynamic meaning you will build a list and then add remove elements from from it
# as your program runs its course for example a game that you create that needs to track the number of montsters 
# on the screen your initial set of monsters can be stored in a list and then as one is destroyed be removed from 
# the list

# modifying elements in a list 
# the syntax for modifying elements in a list is similar to the syntax for accessing an element in a list

# to change an element use the name of the list followed by the index of the element you want to change

# for example we will make a list of motorcycles and we will change an element here is how we would change the value

motorcycles = ['honda','yamaha','suzuki']
# we made a list and now we will print the list and next we will show you how to change the value
print(motorcycles)
# heres how we change values in a list
motorcycles[0] = 'ducati'
print (motorcycles)
# as you can see the first element in the list was changed from honda to ducati
print(motorcycles)
# as you can see this change is permanent

# adding elements to a list
# you might want to add an elements a list for many reasons. for example adding new monsters to a game
# add data to a visalization or add new users to a website registry python provides several ways to do this

# appending elements to a the end of a list
# the simplest way to add a new element to a list is to append the item to the list 
# when you append an item to a list  the new element is added to the end of list 
# in this example we will use the same list to add elements 

# append an item to the end of a list 
motorcycles.append('ducati')
print(motorcycles)

# as we can see we have just added a new element to the end of our motorcycle list
# as you can see the append() method makes it easy to build lists dynamically 
# in our next example we will start with an empty list and build our elements into our list
empty_motorcycle_list = []
empty_motorcycle_list.append('honda')
empty_motorcycle_list.append('yamaha')
empty_motorcycle_list.append('suzuki')
print(empty_motorcycle_list)
# as you can see we built list from scratch 