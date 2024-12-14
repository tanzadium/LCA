def factorial(n):
    A = 1
    for i in range(n):
        A *= i+1
    return A

def taylorExp0(x, k):
    result = 0
    for n in range(k + 1):
        result += (x ** n) / factorial(n)
    return result

if __name__ == '__main__':
    print('taylor_exp0(0,15) =', taylorExp0(0,15))
    print('taylor_exp0(1,15) =', taylorExp0(1,15))
    print('taylor_exp0(2,15) =', taylorExp0(2,15))
    print('taylor_exp0(5,15) =', taylorExp0(5,15))
    print('taylor_exp0(5,10) =', taylorExp0(5,10))