#Lists
# person1="John"
# person2="Mary"
# person3="Bob"
# person4="Alice"
# person_n="Last person"
names=["John", "Mary", "Bob","Alice"] #List. A list is a collection of items in a particular order.
print(names) #Output: ['John', 'Mary', 'Bob', 'Alice']
names.append("Joel") #Add an item to the end of the list.
print(names)
names.insert(3,"Mark") #Insert an item at a given position.
print(names)
names.remove("Mark") #Remove the first item from the list whose value is x. It is an error if there is no such item.
print(names)
names.pop()
print(names)