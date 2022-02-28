number = int(input('inter the wathermelon weight : '))
role = ''
for i in range(1,number+1):
    role += str(i)
for i in range(0, len(role)-1):
    if int(role[i]) % 2 == 0 : 
        if (number -  int(role[i])) % 2 ==0:
            print('Yes')
            break

else:
    print('no')
