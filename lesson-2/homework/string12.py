a = input()
words = a.split('-')
sentence = ''

for x in words:
    sentence += x
    sentence += ' '

print(sentence)


