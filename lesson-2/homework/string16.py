s = input('string: ')
c = input('char: ')
result = ''

for x in s:
    if x != c:
        result += x

print(result)


