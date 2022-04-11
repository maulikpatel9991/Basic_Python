#store data values in key:value pairs.
#ordered*, changeable and do not allow duplicates.

dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
    "year":2020,
    "color":["red","black"]
}
print(dict)
print(type(dict))
print(dict["brand"])
print(len(dict))
print(dict.keys())
print(dict.values())
dict["car"]="white"
print(dict)
print(dict.items())

#########change
dict["year"]="2019"
print(dict)
dict.update({"year":2023})
print(dict)

##############
dict.pop("year")
print(dict)

########
dict.popitem()
print(dict)

for i in dict:
    print(dict[i])

for x, y in dict.items():
    print(x, y)


##############copy ###
dict1 = dict.copy()
print(dict1)

####################nested
my= {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(my)
