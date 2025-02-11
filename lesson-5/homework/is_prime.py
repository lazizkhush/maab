def is_prime(n):
    if n <= 1:
         return False
    for x in range(2, n-2):
        if n%x==0:
                return False
    return True

print(is_prime(2))

