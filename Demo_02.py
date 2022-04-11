'''
Number int,flot,complex
sequencetype = string,list,tuple
Boolean = True , False
Set
Dic
'''

a="Maulik patel"
print(a[:])
print(a[3:5])
print(a[:3])

#List
a=[1,20,3,[1,2,3],4,'maulik']
print(a[1])
print(a[::5])
print(a[1:3])
print(a[1:])
print(a[-4:-1])
print(a[:-1])
print(a[3][2])
a.remove(1)
print(a)
a.pop(1)
print(a)

b=[10,20,30,40,50,60,70,80]

print(b)
print(b[1:5:3]) # [start:stop:step]
print("b")
print(b[1::2])