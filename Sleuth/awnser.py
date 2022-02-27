input = input('ask your question :  ')
vowels =['A', 'E', 'I', 'O', 'U', 'Y']
input = input.replace(' ', '')
input = input.replace('?', '')
if input[-1].upper() in vowels:
    print('yes')
else:
    print('no')
