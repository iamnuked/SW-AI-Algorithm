

def exp(b, n):
    if n == 0:
        return 1

    if n % 2 == 0:
        return exp(b, n/2)*exp(b, n/2)
    else:
        return exp(b, n-1)*b

# print(exp(3, 2))

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)

# print(fib(3))
