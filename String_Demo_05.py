print('a')
print("maulik")

a="patel"
print(a)

b="maulik"
print(b[0])
for i in 'maulik':
    print(i)

# Multiline Strings
d=""" maulik
patel
amiyapur """
print(d)

#len
f=" maulik"
print(len(f))

#check String
g="Ganpat University computer Engineering"
print("Uni" in g)
print("maulik" not in g)

#slicing
m="Patel Maulik""xyz"
print(a[:2])
print(m[1:2])
print(m[:-1])
print(m[-5:])
print(m)

#modify string
n= " patel, maulik "
print(n.upper())
print(n.strip())  #remove white space ex." patel maulik " Ans.patel maulik
print(n.replace("a","mm"))
#####
s=n.split("l")
print(s)
####

a = "Hello"
b = "World"
c = a + " " + b
j=a+b
print(j)
print(c)

###############Format String ###############
l1=100
# t="My En. Number IS " + l1
# print(t)
t1="my En. number is {}"
print(t1.format(l1))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#########Escape
txt1 = "We are the so-called \"Vikings\" from the north."
txt2 = "We are the so-called \\Vikings from the north."
txt3 = "We are the so-called \f Vikings from the north."
txt4 = "We are the so-called \r Vikings from the north."
txt5 = "We are the so-called \ooo Vikings from the north."
print(txt5)
print(txt4)
print(txt3)
print(txt1)
print(txt2)



