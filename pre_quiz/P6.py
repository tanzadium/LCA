def math(a,b):
    
    if a == 0 and b == 0:
        return 'Not defined'
    elif b == 0:
        if a > 0:
            return 'Infinity'
        elif a< 0:
            return 'Negative infinity'
    else:
        return a/b
    
if __name__ == '__main__':
    
    a = float(input('a: '))
    b = float(input('b: '))
    
    r = math(a,b)
    print("a/b = " , r)