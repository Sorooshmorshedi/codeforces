input = [
    10,
    [1, 1, 0, 1, 1, 0, 1, 0, 1, 0]
    ]
houses = input[1]
k = 0
for i in range(1, input[0]-1):
    if houses[i] == 0 and houses[i-1] == 1 and houses[i+1] == 1:
        input[1][i+1] = 0
        k += 1 
print(k)
    
