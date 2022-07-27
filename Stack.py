def menu():
    print("1.insert")
    print("2.Append")
    print("3.delete")
    print("4.sort")
    print("5.reverse")
    print("6.exit")

def insert(list):
    input1  = int(input("enter number"))
    pos = int(input("possion number"))
    list[pos] = input1
    return list

def Append(list):
    input1 = int(input("enter number"))
    list.append(input1)
    return list

def sort(list):
    list.sort()
    return list

def delete(list):
    pos = int(input("possion number"))
    del list[pos]
    return list

def reverse(list):
    list = list[::-1]
    return list

list =[1,2,3,4]
menu()
a = int(input("select Options"))
while True:
    if a == 1:
        list = insert(list)
        print(list)
    elif a == 2:
        list = Append(list)
        print(list)
    elif a == 3:
        list  = delete(list)
        print(list)
    elif a == 4:
        list = sort(list)
        print(list)
    elif a == 5:
        list  = reverse(list)
        print(list)
    elif a == 6:
        break
    else:
        print("choose crrect number")
    menu()
    a = int(input("select"))