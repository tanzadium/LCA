if __name__ == '__main__':
    energy = float(input('Energy( in kcal):')) #1kcal = 4184 J
    J = energy * 4184 # Change kcal to J
    Wh = J/3600 # Change J to Wh
    
    print("That is {:.2f} J or {:.2f} Wh.".format(J, Wh))