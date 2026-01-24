from ec import *



def main():
    a1 = E[0]
    a2 = E[1]
    a3 = E[2]
    a4 = E[3]
    a6 = E[4]

    b2 = a1**2 + 4*a2
    b4 = 2*a4 + a1*a3
    b6 = a3**2 + 4*a6
    b8 = a1**2 * a6 + 4*a2*a6 - a1*a3*a4 + a2*a3**2 - a4**2


    x = Symbol('x')
    y = Symbol('y')
    # \psi_3 = 3x^4 + b2 x^3 + 3b4 x^2 + 3b6 x + b8
    psi3 = Poly([3,b2,3*b4,3*b6, b8], x)

    # \psi_2 = 2y + a_1 x + a3
    psi2sq = Poly([4,b2,2*b4,b6], x)
    psi4bypsi2 = Poly([2,b2,5*b4,10*b6,10*b8,(b2*b8-b4*b6),(b4*b8-b6**2)], x)
    
    phi3 = x*psi3**2-psi2sq*psi4bypsi2

    

    return roots(psi3)

    return



if __name__ == '__main__':
    main()