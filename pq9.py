#9)) What is data type SET in Python and how to work with it?

''' The Python data type “set” is a kind of collection. It has been part of Python since version 2.4.
A set contains an unordered collection of unique and immutable objects.'''


# Create a set with strings and perform a search in set
objects = {"python", "coding", "tips", "for", "beginners"}

# Print set.
print(objects)
print(len(objects)) 

# Use of "in" keyword.
if "tips" in objects:
    print("These are the best Python coding tips.")

# Use of "not in" keyword.
if "Java tips" not in objects:
    print("These are the best Python coding tips not Java tips.")

# *** Lets initialize an empty set
items = set()

# Add three strings.
items.add("Python")
items.add("coding")
items.add("tips") 

print(items)

