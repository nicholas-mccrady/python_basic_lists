import random
# you can use individual values from a list just as you would any other variable
# one example is that you can use f-strings to create a message based on a value from a list

bicycles = ['trek','cannondale','redline','specialized']
# again f-strings allow use to format variables into a string

# we are assigning bicycles to the variable "message"
message = f"my first bicycle was a {bicycles[0].title()}."
# we created an f-string and we are adding the bicycle variable to the string and then we are 
# calling the title method on the list and we are telling python that we want the first element of the list
# from bicycles
print(message)

# here are a couple of demonsrations of what we went over
names = ['tom','bob','sam']
print(names[0])
print(names[1])
print(names[2])

# greeting practice
# remember your braces and parenthisis for your variable and your method
# also you must pass the element into a varible if you want to use a method on it or display it
greeting_name = f"Greetings {names[0].title()}"
print(greeting_name)
# remember pass it to a variable ex line 23 

# one more example using destination 
destinations = ['beach','zoo','airport']
# example using the random method on a destination
my_destination = random.choice(destinations)
print("I want to goto the", my_destination)
print(destinations[1])

