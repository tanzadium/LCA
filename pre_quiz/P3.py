if __name__ == '__main__':
    v = float(input('Enter voltage (V): '))
    i = float(input('Enter current (A): '))
    h = float(input('Enter operating time (h): '))
    p = v*i #power
    e = p*h #energy
print('The energy consumed is {:,.1f} Wh'.format(e))
