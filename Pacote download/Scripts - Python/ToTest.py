from math import sqrt
n = 0  # size of sample
sigma = 0  # standard deviation
mu = 0  # mean of sample
x = 0
SE = 0  # standard error
delta = 0  # margin of error
pSample = 0  # proportion in the sample
pdelta = 0  # error in population
nProp = 0  # size of proportion
s = 0  # value S for pop estimation
z = 0  # confidence parameter
choice = str(input('''
            What do you want, motherfucker? 
            d for delta (margin of error)
            n size of population (without proportion)
            z for confidence parameter
            p for population margin
            m size of population (with proportion)
'''))
if choice in 'dD':
    z = float(input('Z = '))
    sigma = float(input('sigma = '))
    n = float(input('n = '))
    SE = sqrt((sigma * sigma) / n)
    delta = z * SE
    print(f'Delta = {delta} e SE = {SE}')
    choice = str(input(f'Do you want the interval, sucker? [s/n]'))
    if choice in 'sS':
        mu = float(input('mean = '))
        print(f'interval = ({mu - delta},{mu + delta})')
elif choice in 'nN':
    z = float(input('Z = '))
    sigma = float(input('sigma = '))
    delta = float(input('delta = '))
    n = ((z*z) * sigma * sigma)/(delta*delta)
    print(f'n = {n}')
elif choice in 'zZ':
    sigma = float(input('sigma = '))
    delta = float(input('delta = '))
    n = float(input('n = '))
    num = n/sigma*sigma
    z = delta * sqrt(num)
    print(f'Z = {z}')
elif choice in 'pP':
    pSample = float(input('p = '))
    n = float(input('n = '))
    z = float(input('Z = '))
    s = pSample * (1-pSample)
    num = s / n
    SE = sqrt(num)
    pdelta = z * SE
    print(f'Delta of p = {pdelta}')
elif choice in 'mM':
    pSample = float(input('p = '))
    z = float(input('Z = '))
    SE = float(input('Accepted error = '))
    s = pSample * (1 - pSample)
    n = (z * z * s) / (SE * SE)
    print(f'n = {n}')
