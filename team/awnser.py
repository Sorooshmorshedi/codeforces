input = [
    5,
    [1, 1, 0],
    [1, 1, 1],
    [0, 0, 0],
    [1, 0, 1],
    [1, 0, 0]
]   
implements = 0
for i in range(1,input[0]+1):
    counter = 0
    for x in input[i] :
        if x == 1:
            counter += 1
        
    if counter >= 2:
        implements += 1 
print(implements)
