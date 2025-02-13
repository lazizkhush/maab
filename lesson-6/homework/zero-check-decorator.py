def check(func):
    def wrapper(a, b):
        if b==0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper

try:
    a = int(input('a = '))
    b = int(input('b = '))
except:
    print('Invalid input')

@check
def div(a, b):
    return a/b

print(div(a, b))

