def factorial1(N):
    prod = 1
    for i in range(1, N+1):
        prod *= i
    return prod

def pow2(N):
    return N ** 2

pow3 = lambda x: x ** 3

def mirror(f, x):
    return f(x)


if __name__ == '__main__':
    print(pow3(4))
