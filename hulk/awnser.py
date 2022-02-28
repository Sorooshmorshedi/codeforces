input = int(input('inter your number : '))
final_output = ''
for i in range(1, input+1):
    if i % 2 == 0:
        final_output += 'I like that '
    else:
        final_output += 'I hate that '
print(final_output)
