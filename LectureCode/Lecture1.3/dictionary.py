#Dictionary
person1 = {
  "name": "John",
  "age": 30, 
  "city": "New York"
           }
#Dictionary. A dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
my_name=person1["name"]
print(my_name)
name=person1.get("name")
print(name)
print(person1) #Output: {'name': 'John', 'age': 30, 'city': 'New York'}
person1["name"]="Mark" #Change the value of a specific item.
print(person1)
person1["email"]="example@gmail.com"
print(person1)
del person1["email"] #Remove the item with the specified key name.
print(person1)

#Keys in a dictionary.
keys=person1.keys()
print(keys)

#Values in a dictionary.
values=person1.values()
print(values)

#Items in a dictionary.
items=person1.items()
print(items)