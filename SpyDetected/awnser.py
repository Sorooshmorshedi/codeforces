input = [
    5,
    4,
    [11, 11, 13, 11],
    5,
    [4, 4, 7, 4, 4],
    10,
    [3, 3, 3, 3, 10, 3, 3, 3, 3, 3],
    4,
    [11, 11, 11, 18],
    3,
    [20, 20, 10],
]   

for i in range(1, input[0]+1):
    dic = {}
    numbers = []
    for x in input[i*2]:
        if not x in numbers:
            numbers.append(x)
            dic[x] = 1
        else: 
            dic[x] += 1
            
    for num in dic:
        if dic[num] == 1:
            x = 1
            for value in input[i*2]:
                if value == num:
                    print(x)
                x += 1
        
    
    
