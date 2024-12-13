import math

if __name__ == '__main__':

    N = int(input('Number of  values:'))
    sum_squared = 0
    
    for i in range (N):
        v = float(input('value:'))
        sum_squared += v**2
        
    rms = math.sqrt((sum_squared/N))
    print('RMS = {:,.2f}'.format(rms))