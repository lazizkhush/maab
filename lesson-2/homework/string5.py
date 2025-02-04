a = input()

vowel = 0
con = 0
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(len(a)):
    if a[i] in vowels:
        vowel+=1
    else:
        con+=1

print(f'{vowel=}')
print(f'{con=}')
