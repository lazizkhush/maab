txt = input("txt = ")
repl = input('replace the word ')
repl_with = input('replace with ')
result = ''
splitted = txt.split(' ')
contains = False
for i in range(len(splitted)):
    if splitted[i]==repl:
        splitted[i]=repl_with
        contains = True
if contains:
    for x in splitted:
        result+=x
        result+=" "

print(result) 
