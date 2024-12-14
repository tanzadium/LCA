def factorial(n):
    A = 1
    for i in range(n):
        A *= i+1
    return A

def taylorSin0(x ,k):
    result = 0
    for n in range(k + 1):
        if n % 2 == 1:
            term = ((-1)**((n-1)//2) * x**n) /factorial(n)
            result += term
    return result

def taylorSinHalfpi(x, k):
    result = 0
    for n in range(k + 1):
        if n % 2 == 0:  
            term = ((-1)**(n//2) * (x - 3.141592653589793/2)**n) / factorial(n)
            result += term
    return result

def taylorCos0(x, k):
    result = 0
    for n in range(k + 1):
        if n % 2 == 0: 
            term = ((-1)**(n//2) * x**n) / factorial(n)
            result += term
    return result

if __name__ == '__main__':
    pi = 3.141592653589793
    print('taylor_sin0(pi/4, 4)=', taylorSin0(pi/4, 4))
    print('taylor_sin_halfpi(pi/4, 4)=', taylorSinHalfpi(pi/4, 4))
    for x in [0, pi/6, pi/2, pi, pi*2]:
          print(("x = {:.2f}: sin:0,k15 = {:.4f}, " + \
                  "sin:pi/2,k15 = {:.4f}").format(x, taylorSin0(x, 15),
                                              taylorSinHalfpi(x, 15)))
    print('\ntaylor_cos0(pi/4, 4)=', taylorSin0(pi/4, 4))
    for x in [0, pi/6, pi/2, pi, pi*2]:
          print("x = {:.2f}: cos:0,k15 = {:.4f}".format(x, taylorCos0(x, 15)))