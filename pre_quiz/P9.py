if __name__ == '__main__':
    
    battery_operating = 12 #volt
    capacity = float(input('Battery capacity (mAh):'))
    calculate = battery_operating * (capacity/1000)

    print('At its 12 V rating, it stores %.2f Wh.'%calculate)