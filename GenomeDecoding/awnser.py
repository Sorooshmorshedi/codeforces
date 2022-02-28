length = int(input('inter len of  Genome : '))
genome = input('inter the  Genome : ')

if length % 4 != 0:
    print('===')
else:
    t = genome.count('T')
    a = genome.count('A')
    g = genome.count('g')
    c = genome.count('C')
    T = length/4 - t
    A = length/4 - a
    G = length/4 - g
    C = length/4 - c            

    final_output = ''
    for i in genome:
        if g > length/4 or t > length/4 or a > length/4 or c > length/4:
            print('===')
            break

        if i != '?':
            final_output += i   
        elif i == '?':
            if T > 0:
                final_output += 'T'
                T -= 1
            elif A > 0:
                final_output += 'A'
                A -= 1  
            elif G > 0:
                final_output += 'G'
                G -= 1
            elif C > 0:
                final_output += 'C'
                C -= 1
    print(final_output)  
