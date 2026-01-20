# E: y^2 = f(x)

# f = [a2, a1, a0] <-> f(x) = x^3 + a2 x^2  + a1 x + a0
from ec import *
from sympy.ntheory.factor_ import core

# given (integral for now) x, find the residue field for (x, sqrt(f(x)))
# return m = squarefree part of f(x) (so residue field is Q(sqrt(m)))
def findQuad(f,x):

    eval = x**3 + f[0]*x**2 + f[1] * x + f[2]
    if eval < 0:
        return -1*core(-1*eval, 2)

    elif eval == 0:
        return 0

    return core(eval, 2)

# check if the appropriate min poly factors over fp
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


def main():
    exes = []
    for i in range(0,7):
        # exes.append(4+7*i)
        # exes.append(5+7*i)
        exes.append(i)

    # throughout: an elliptic curve E with Weierstrass equation: y^2 + a1 xy + a3 y = x^3 + a2 x^2 + a4 x + a6
    
    # will be stored as E = [a1, a2, a3, a4, a6]
    # f(x) = x^3 + x^2 - 13x + 15
    


    # f = [1,-13,15] # 172a

    # f = [-1,3,9] # 228.a1

    f = [1,-9,-13] # 209.a2
    E = [0,f[0],0,f[1],f[2]]

    for x in exes:
        m = findQuad(f,x)
        print(x, m, splitCompletely(m,7))


    # [0,f[0], 0, f[1], f[2]]
    print(getFpPointOrders(E, 7))

    # P = [2,3]
    # Q = P
    # done = False

    # take powers of P until hit infinity
    # while not done:
    #     Q = ellMultFp([0,0,0,0,1],P,Q,7)
    #     print(Q)
    #     if Q == 'infinity':
    #         done = True

    # print(getFpPoints([0,0,0,0,1], 7))
    return

if __name__ == "__main__":
    main()