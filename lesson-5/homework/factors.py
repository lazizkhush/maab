def factors(n):
    for x in range(1, n+1):
        if n%x==0:
            print(f'{x} is a factor of {n}')

while True:
    try:
        num = int(input("Enter a positive integer: "))
        if (num<=0):
            print("Invalid input")
        else:
            factors(num)
            break
    except:
        print('Enter an integer')

