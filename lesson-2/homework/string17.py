a = input()
result = ''
vowels = ['a', 'e', 'i', 'o', 'u']
for x in a:
    if x in vowels:
        result += '*'
    else:
        result += x

print(result)    
