a = input()
words = a.split(' ')
acr = ''
for x in words:
    acr += x[0].upper()
print(acr)