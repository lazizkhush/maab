isstrong = False
while not isstrong:
    password = input('Enter a password: ')
    long_enough = True
    if len(password)<8:
        print('Password is too short')
        long_enough = False
    contains_upper = False
    for char in password:
        if char.isupper():
            contains_upper = True
    if not contains_upper:
        print('Password must contain an uppercase letter.')


    if long_enough and contains_upper:
        isstrong = True
        print('password is strong')
