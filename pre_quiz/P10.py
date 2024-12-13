if __name__ == '__main__':
    
    bc = float(input('Battery capacity (Wh):'))
    idle = float(input('average power (idle, mW):'))
    norm = float(input('average power (normal, mW):'))
    
    ot_idle = bc/(idle/1000) # ot stand for operating time
    ot_norm = bc/(norm/1000) # ot stand for operating time
    
    print('The battery will last %.0f hrs in idle mode.'%ot_idle)
    print('The battery will last %.1f hrs in normal mode.'%ot_norm)