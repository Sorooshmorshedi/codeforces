input1 = int(input('inter first number  :  '))
input2 = int(input('inter second number  :  '))
number = input1 / input2
left = input1 % input2
if left == 0:
    for i in range(0, input2):
        print(int(number))
elif left != 0:
    x = 0
    for i in range(0, input2):
        if x < left:
         print(int(number) + 1)
         x += 1
        else :
            print(int(number))
            
         
