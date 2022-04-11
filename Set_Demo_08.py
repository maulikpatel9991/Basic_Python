#Set is a collection which is unordered, unchangeable*, and unindexed.
# No duplicate allow
# set duplicate value is not count
#You cannot access items in a set by referring to an index or a key.
#pop first remove not last and first
set={"maulik",'anjali',"Patel",'maulik'}
print(set)
print(type(set))
print(len(set))
print('maulik' in set )
for i in set:
    print(i)

#####set Add()######
a={1,2,3,4,5}
b={7,8,9}
a.add(1000000)
b.update(a)
print(b)
a.add(10)
print(a)

#######remove() pop()#####
c={1,2,3,4,5}

c.remove(4)
print(c)
c.pop()
print("pop item",c)
###########POP ####################
d={"maulik","atel","Ayz"}
d.pop()
print(d)
#################################

d={10,2,3,4,5,}
for i in d:
    print(i)

#############joi set ###########
f={1,2,3,4}
f1={5,6,7,8,4}
f2=f1.intersection(f)
f3=f1.union(f)
print(f3)
print(f2)


#####################################🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
x={1,2,3,4}
x.add(100000) # add first in set 100000
x.add(100)   # add last in set 100
print(x)
########################🙄🙄🙄🙄🙄🙄🙄🙄