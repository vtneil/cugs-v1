def factorial1(N):
    prod = 1
    for i in range(1, N+1):
        prod *= i
    return prod

def factorial2(N):
    if N == 0:
        return 1
    return N * factorial2(N-1)


if __name__ == '__main__':
    print(factorial2(5))
