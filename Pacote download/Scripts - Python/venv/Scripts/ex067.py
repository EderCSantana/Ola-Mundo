while True:
    n = int(input('Voce quer a tabuada de qual número? '))
    print(f'''A tabuada de {n} é:
                n x 0 = 0
                n x 1 = {n}
                n x 2 = {2*n}
                n x 3 = {3*n}
                n x 4 = {4*n}
                n x 5 = {5*n}
                n x 6 = {6*n}
                n x 7 = {7*n}
                n x 8 = {8*n}
                n x 9 = {9*n}
                n x 10 = {10*n}
                ''')
    if n < 0:
        break
        print('Flw, vlw')
