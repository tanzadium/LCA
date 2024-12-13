if __name__ == '__main__':
    v = float(input('Enter voltage (V): '))
    i = float(input('Enter current (A): '))
    h = float(input('Enter operating time (h): '))
    p = v*i #Power
    e = p*h #Energy
    u = e/1000 #unit
    c = u*4 #cost per unit
    
print('The cost is {:,.2f}'.format(c))