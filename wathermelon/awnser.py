number = int(input('inter the wathermelon weight : '))
role = [i for i in range(1, number+1)]
for i in role:
    if i % 2 == 0 : 
        if (number -  i) % 2 == 0:
            print('Yes')
            break
else:
    print('no')
