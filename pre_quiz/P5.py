def power_equiv(watt):
    hp = (watt/745.7)  # 1 hp = 745.7 w
    btum = (watt/0.293)  # 0.293 w = 1btu/h 1/0.293
    calm = (watt*14.33)  # 1 watt = 14.33 calm
    erg = (watt*1e7)  # 1 watt = 1e7 erg
    flbm = (watt*44.25)  # 1 watt 44.25 foot pound-force/minute
    return hp, btum, calm, erg, flbm

if __name__ == '__main__':
    pwatt = 100
    horsep, btuh, calmin, perg, footlbm = power_equiv(pwatt)
    print(pwatt, 'w =', round(horsep,3), 'hp =',
        round(btuh,3), 'btu/h =',
        round(calmin,3),'cal/min =',
        round(perg,3), 'erg =',
        round(footlbm,3), 'f-lb/min')    