# mostly a copy of doublecover.ipynb

from ec import *

def getHyperFpPoints(E, p):
    pts = {}
    pts['infinity'] = 2 # include the point at infinity

    # reduce coefficients mod p
    a1 = rationaltoFp(E[0], p)
    a2 = rationaltoFp(E[1], p)
    a3 = rationaltoFp(E[2], p)
    a4 = rationaltoFp(E[3], p)
    a6 = rationaltoFp(E[4], p)

    # check all pairs (x,y) in Fp x Fp
    for x in range(p):
        for y in range(p):
            # check if equation is satisfied mod p
            if (( (y**2)%p + (a1*x*y)%p + (a3*y)%p)%p == ((x**6)%p + a2*(x**4)%p + a4*(x**2)%p + a6)%p ):
                pts[(x,y)] = 0
    return pts


def getSquares(p):
    squares = []
    for i in range(p):
        sq = (i**2) % p
        if not sq in squares:
            squares.append(sq)

    squares.sort()
    return squares

def getImage(p):
    image = []
    for i in range(p):
        sq = (i**2 + i + 1) % p
        if not sq in image:
            image.append(sq)

    image.sort()
    return image

def check(p):

    print("checking for p =", p)
    # elliptic curve and mw gen
    E = [0, 0, 1, -3834, -91375]
    gen = [Fraction('-143/4'), Fraction('-3/8')]
    
    # get Fp points and their orders
    pts= getFpPoints(E, p)
    N = len(pts)
    print('#E(F_p) =',N)
    # print(orders)
    
    # get the image of E(Q) = <gen> mod p
    image = subgroupModP(E,gen,p)
    m = len(image)
    print('#E(Q) =', m)
    print('index =', N/m)
    
    # to check x coords
    # squares= getSquares(p) #q = x^2
    squares= getImage(p) #q = x^2+x+1

    

    print('\nfor pts in E(Q):')
    # check points in image of E(Q)
    splitct = 1 # fiber at infinity 
    inertct = 0
    ramct = 0
    gather = True
    for pt in image:
        
        if pt != 'infinity':
            # if pt[0] == 0:
            #     ramct += 1
                # gather = False
                # break
            if pt[0] in squares:
                splitct +=1
            else:
                inertct += 1
    # print(squares)
    if gather:
        print("split:", splitct)
        print("inert:", inertct)
        print("ramified:", ramct)

    print('\nfor pts in E(F_p):')
    # check all E(F_p) points
    totalsplitct = 1 # fiber at infinity 
    totalinertct = 0
    totalramct = 0
    gather = True
    for pt in pts:
        
        if pt != 'infinity':
            # if pt[0] == 0:
            #     totalramct += 1
                # gather = False
                # break
            if pt[0] in squares:
                totalsplitct +=1
            else:
                totalinertct += 1
    # print(squares)
    if gather:
        print("split:", totalsplitct)
        print("inert:", totalinertct)
        print("ramified:", totalramct)


    print('\n')
    # print(getHyperFpPoints(E,p))
    return N,m,splitct,inertct,ramct,totalsplitct, totalinertct, totalramct

def checkv2(p):

    print("checking for p =", p)

    # E = [0, 0, 1, -3834, -91375]
    # gens = [[Fraction('-143/4'), Fraction('-3/8')]]
    # checking 189.b3 (not 189.b1)
    E = [0, 0, 1, -54, -88]
    gens = [[Fraction('-6'), Fraction('4')], [Fraction('12'), Fraction('31')]]
    
    # get Fp points and their orders
    pts= getFpPoints(E, p)
    N = len(pts)
    print('#E(F_p) =',N)
    # print(orders)
    
    # get the image of E(Q) = <gens mod p>
    image = subgroupModPv2(E,N,gens,p)
    m = len(image)
    print('#E(Q) =', m)
    print('index =', N/m)
    
    # to check x coords
    squares= getImage(p)
    

    print('\nfor pts in E(Q):')
    # check points in image of E(Q)
    splitct = 1 # fiber at infinity 
    inertct = 0
    ramct = 0
    gather = True
    for pt in image:
        
        if pt != 'infinity':
            # if pt[0] == 0:
            #     ramct += 1
                # gather = False
                # break
            if pt[0] in squares:
                splitct +=1
            else:
                inertct += 1
    # print(squares)
    if gather:
        print("split:", splitct)
        print("inert:", inertct)
        print("ramified:", ramct)

    print('\nfor pts in E(F_p):')
    # check all E(F_p) points
    totalsplitct = 1 # fiber at infinity 
    totalinertct = 0
    totalramct = 0
    gather = True
    for pt in pts:
        
        if pt != 'infinity':
            # if pt[0] == 0:
            #     totalramct += 1
                # gather = False
                # break
            if pt[0] in squares:
                totalsplitct +=1
            else:
                totalinertct += 1
    # print(squares)
    if gather:
        print("split:", totalsplitct)
        print("inert:", totalinertct)
        print("ramified:", totalramct)


    print('\n')
    # print(getHyperFpPoints(E,p))
    return N,m,splitct,inertct,ramct,totalsplitct, totalinertct, totalramct

    
def main():

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
              101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
              211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
              307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
              401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
              503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
              601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
              701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
              809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
              907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997,
              1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 
              1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 
              1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 
              1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 
              1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 
              1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 
              1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 
              1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 
              1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 
              1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999
              ]    
    # primes = [13]
    writefile = open("newdata/cheb6.txt", "w")
    # avoid primes of bad reduction
    
    writefile.write('#E(F_p)\t#E(Q)\tindex\ntotalsplit\ttotalinert\ttotalramified\ttotalsplitpercentage\nsplit\tinert\tramified\tsplitpercentage\n')
    for p in primes:
        if p!= 3 and p!=7:
            N,m, splitct,inertct,ramct,totalsplitct, totalinertct, totalramct = checkv2(p)
            writefile.write('p = '+ str(p))
            writefile.write('\n')
            
            writefile.write(str(N)+'\t'+str(m)+'\t'+str(int(N/m))+'\n'
                            +str(totalsplitct)+'\t'+str(totalinertct)+'\t'+str(totalramct)+'\t'+str(totalsplitct/N)+'\n'
                            +str(splitct)+'\t'+str(inertct)+'\t'+str(ramct)+'\t'+str(splitct/m)+'\n')

main()