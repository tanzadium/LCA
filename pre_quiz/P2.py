if __name__ == "__main__":
    p = float(input('Enter power in watt:'))
    h = float(input('Enter operating hours:'))
    e = p*h #energy
    j = 3600*e #จูล
print('Energy = {:,.2f} Wh or {:,.2f} J'.format(e,j))