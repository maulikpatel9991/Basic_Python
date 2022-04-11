# lists are mutable.
#Once a list has been created: Elements can be modified.
#List items are ordered, changeable, and allow duplicate values list and Tuple And not allow in set
#first item has index [0]


list = ["apple", "banana", "cherry","apple"]
print(list)
print(type(list))
print(len(list))
print(list[1:])
print(list[:-1])


#change list
list[1]="maulik"
print(list)
list.insert(1,"patel")
print(list)

#Add List
l = ["apple", "banana", "cherry","apple"]
l.append("xyz")
l.insert(10,"zzz")
print(l)
print(l)
##########
l2 = ["apple", "banana", "cherry"]
l3 = ["mango", "pineapple", "papaya"]
l3.extend(l2)
print(l3)

#convert tuple to list
a=[1,2,3,4]
b=(5,6,7)
a.extend(b)
print(a)
#######
c=[1,2,3,4,5]
# c.clear()
f=c.index(1)
print("maulik is",f)
print(c)
print(c.pop(4))
d=c.pop()
print(d)

######for loop using list #######
print("For loop using List")
List5=[10,2,3,4,5]
for i in List5:
    print(i)
for i in range(len(List5)):
    print("Index")
    print(List5[i])

###########List Comprehension ################
fruits = ["apple","mango", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "ap" in x:
    newlist.append(x)

print(newlist)

#######list Sort #######
#Python Case sensitive sort
fruits.sort()
print(fruits)

this = [100, 50, 65, 82, 23]

this.sort(reverse = True)
print(this)
this.reverse()

print(this)

######COPY LIST #####
l1=[1,2,3,4]
l2=l1.copy()
print(l2)


##########join list ##########
d=[1,2,3,4]
f=[5,6,7]
d1=d+f
print(d1)
d.extend(f)
print(d)

##count
m=[1,2,3,4,5,6,3,4,56,]
print(m.count(3))
