def factorial(n):
    if n ==0 or n ==1:
        return 1
    return n * factorial(n-1)

if __name__ == '__main__':
    print('Factorial(12) = ', factorial(12))
    for i in range(8):
        print('i=', i, '; factorial =', factorial(i))