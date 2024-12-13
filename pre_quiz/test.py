import math # math.sqrt may be handy.
if __name__ == '__main__':
    N = int(input('Number of values:'))
    v = []
    for i in range(N):
        j = float(input("value:"))
        v.append(j)
    ss = 1
    sig = 0
    for i in v :
        sig = sig + i**2
    rms = math.sqrt((ss/N)*sig)
    print('RMS = {:,.2f}'.format(rms))