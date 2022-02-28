input = [
4,
[1, 2, 3, 5],
[1, 2, 3, 6],
[5, 2, 6, 27],
[3, 3, 5, 18]
]

cases = input[0]

for i in range(1, cases+1):
    case = input[i]
    a = input[i][0] ; b = input[i][1] ; n = input[i][2] ; s = input[i][3]
    if (a*n) + b == s:
        print('YES')
    else:
        print('NO')
    
