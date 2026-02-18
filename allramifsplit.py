# X: y^2 = f(x) = x(x-1)...(x-(p-1))


from ec import *
from sympy.ntheory.factor_ import core

# given (integral for now) x, find the residue field for (x, sqrt(f(x)))
# return m = squarefree part of f(x) = x(x-1)*...(x-(p-1)) (so residue field is Q(sqrt(m)))
def findQuad(p,x):

    eval = 1
    for i in range(p):
        eval *= (x-i)


    if eval < 0:
        return -1*core(-1*eval, 2)

    elif eval == 0:
        return 0

    return core(eval, 2)

# check if the appropriate min poly factors over fp
# this is equivalent to checking if f(x) is a square mod p (or separately zero)
# fine for now
def splitCompletely(m, p):
    distinctFactors = False
    roots = []
    
    if m % 4 == 1:
        # check x^2 - x + (1-m^2)/4    
        for i in range(p):
            if (i**2 - i + (1-m^2)//4)%p == 0:
                roots.append(i)

    else:
        # check x^2 - m
        for i in range(p):
            if (i**2 - m)%p == 0:
                roots.append(i)
    
    if len(roots) == 0:
        return "remains prime"
    
    elif len(roots) == 1:
        return "ramified"
    elif len(roots ) == 2:
        return "splits"

    return distinctFactors



def v(p,x):
    if x ==0  or x % p != 0:
        return 0
    else:
        return 1 + v(p, x//p)


def main():
    p = 7
    exes = []
    for i in range(0,200):
        
        # exes.append(i)

        # if v(t,B) = 2
        if v(p,i) % 2 == 1:
            exes.append(p*i)


    for x in exes:
        m = findQuad(p,x)
        # print(x, m, splitCompletely(m,p))
        print(x, splitCompletely(m,p))

    return

if __name__ == "__main__":
    main()