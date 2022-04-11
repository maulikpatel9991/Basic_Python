#A tuple is a collection which is ordered and unchangeable.
#tuples are immutable.
#Tuple items are ordered, unchangeable and allow duplicate values.

a=("maulik","patel","Ravi","Patel","Parth")
print(a)
print(type(a))

x1 = a.index("maulik")
print("maulik:::",x1)
print(a[1])
print(a[:-1])
print(a[-1])
print(a[2:4])

#####add items in tuple#####
x=list(a)
x.append("xyx")
a=tuple(x)
print(x)

##########Unpacking a Tuple ##########
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
fruits1 = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits1

print(green)
print(tropic)
print(red)

######################for loop ################
a1 = (1,2,3,4,5)
for i in range(len(a1)):
    print(a1[i])
