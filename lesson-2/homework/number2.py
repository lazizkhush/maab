a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if (a>b and a>c):
    largest = a
elif (b>a and b>c):
    largest = b 
else:
    largest = c

if (a>b and c>b):
    smallest = b
elif (b>a and c>a):
    smallest = a 
else:
    smallest = c  

print(f"{largest=} ")
print(f"{smallest=} ")

