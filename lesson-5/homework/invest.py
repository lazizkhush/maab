def invest(amount, rate, years):
    rate += 1
    for i in range(1, years+1):
        print(f'year {i}: {amount*(rate**i):.2f}')


amount = int(input("Amount: "))
rate = float(input("Rate: "))
year = int(input('Years: '))

invest(amount, rate, year)

