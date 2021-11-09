#Tuple is a data type which will allow multiple values with difft data types assigned to a variable but it is Immutable
T1 = (1,2,"hello there",4.5)
print(T1)
print(T1[0]) ## gives the first value of list
print(T1[-1]) ## gives the last value of a list
print(T1[1:-1]) ## to get a sublist. it will always display last index-1 value only


#to get the  number of times an item is avialable
print(T1.count(4.5))

###initialise and print a dictionary
dict1 = {"a": 1, 2: "Seema", "b" : "Jelly Belly"}
print(dict1["a"])
print(dict1[2])
print(dict1["b"])
print(dict1)

###how to put values into a dictionary at run time
dict2 = {}
dict2["firstname"] = "Revathi"
dict2["lastname"] = "Srinagesh"
dict2["age"] = 36
print(dict2)

##to print the keys
print(dict2.keys())

# to print everyhthing in a dictionary
print(dict2.items())

#removes the last item form the dictionary
print(dict2.popitem())
print(dict2)

# remove any 1 item from dict
print(dict1.pop("a"))
print(dict1)

#to add more data using update
dict2.update({"age": 35})
print(dict2)

