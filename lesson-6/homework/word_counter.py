try:
    open('sample.txt')
except FileNotFoundError:
    print('File does\'nt exist')
    text = input('Enter a pragraph to create sample.txt')
    with open('sample.txt', 'w') as f:
        f.write(text)

with open('sample.txt', 'r') as f:
    words = f.read().lower().replace(',', '').replace('.', '').replace('?', '')\
    .replace('!', '').replace('\n', ' ').split()


freq = {}
for x in words:
    count = 0
    for i in words:
        if x==i:
            count+=1
    freq[x] = count
print("Word count report")
print(f'Total words {len(words)}')

top_words = dict(sorted(freq.items(), key=lambda item:item[1], reverse=True))
n_words = int(input('How many top number you want to display? : '))
print(f'Top {n_words} words')

i = 0
for word, count in top_words.items():
    if i != n_words:
        print(f'{word} - {count}')
        i+=1
    
    