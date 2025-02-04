a = input('String: ')
starts_with = input('Starts with: ')
ends_with = input('Ends with: ')

words = a.split(' ')
print(f'Starts with {starts_with}:', starts_with==words[0])
print(f'Ends with {ends_with}:', ends_with==words[-1])


