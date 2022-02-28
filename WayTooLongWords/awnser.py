number = int(input('inter the number of inputs : '))
inputs = []
for i in range(0,number):
    my_input = input('inter a word : ')
    inputs.append(my_input)
for word in inputs:
    if len(word) > 10:
        my_word = word[0] + str(len(word) - 1) + word[-1]
        print(my_word)
    else:
        print(word)
