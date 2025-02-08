string = input()
result = ''
end = 3
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(0, len(string), 3):
    if not end>=len(string):
        if string[end-1] in vowels:
            result+=string[i:end+1]+'_'
        else:
            result+=string[i:end]+'_' 
        end+=3
        
    else:
        result += string[i:]     
print(result)

