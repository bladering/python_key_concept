print("please input three numbers\n")
n1 = input("please input number 1:")
n2 = input("please input number 2:")
n3 = input("please input number 3:")

lst = [int(n1),int(n2),int(n3)]

for i in range(3):

    if lst[0] > lst[1] :
        tmp = lst[0] 
        lst[0] = lst[1]
        lst[1] = tmp
    else:
        pass


    if lst[1] > lst[2] :
        tmp = lst[1]
        lst[1] = lst[2]
        lst[2] = tmp
    else:
        pass

print(lst)    
