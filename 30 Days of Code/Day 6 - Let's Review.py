n = int(input('How many strings will you input?: ').strip())
#strings = {}
for i in range(1,n+1):
    #key = f'Word {i}' #testing use of f-strings
    input_string = str(input(f'Inpute word {i}: ').strip())
    #strings[key] = value
    even = input_string[::2]
    odd = input_string[1::2]
    print(f'{even} {odd}')

#print(strings)
