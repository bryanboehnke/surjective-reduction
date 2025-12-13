from fractions import Fraction

# throughout: an elliptic curve E with Weierstrass equation: y^2 + a1 xy + a3 y = x^3 + a2 x^2 + a4 x + a6
# will be stored as E = [a1, a2, a3, a4, a6]

# p is a prime, x is a Fraction (representing an element of Z_p)
# returns x mod p
def rationaltoFp(x, p):
    return ((x.numerator %p) * (x.denominator % p)**(p-2) ) % p


# E elliptic curve, p prime
# Fp points stored as dictionary with points as keys (whose values will be eventually incremented when reduced to mod p)
def getFpPoints(E, p):
    pts = {}
    pts['infinity'] = 1 # include the point at infinity

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
            if (( (y**2)%p + (a1*x*y)%p + (a3*y)%p)%p == ((x**3)%p + a2*(x**2)%p + a4*x + a6)%p ):
                pts[(x,y)] = 0
    return pts


# reference: Silverman AEC III.2.3
# E elliptic curve, P and Q points on E
# return P*Q
def ellMult(E, P, Q):
    if P == "infinity":
        return Q
    if Q == "infinity":
        return P

    # casting coordinates to rational numbers 
    x1 = Fraction(str(P[0]))
    y1 = Fraction(str(P[1]))

    x2 = Fraction(str(Q[0]))
    y2 = Fraction(str(Q[1]))

    a1 = Fraction(str(E[0]))
    a2 = Fraction(str(E[1]))
    a3 = Fraction(str(E[2]))
    a4 = Fraction(str(E[3]))
    a6 = Fraction(str(E[4]))

    # if Q = -P, then P + Q = O
    if x1 == x2 and y1 + y2 + a1 * x2 + a3 == 0:
        return "infinity"

    # y = mx + b is the line through P and Q

    # if P = Q, take the tangent line at P
    if P == Q:
        m = Fraction(3*x1**2 + 2*a2*x1 + a4 - a1*y1, 2*y1 + a1*x1 + a3)
        b = Fraction(-1*x1**3 + a4*x1 + 2*a6 - a3*y1 , 2*y1 + a1*x1 + a3)
    
    # otherwise, point-slope formula does the trick
    else:
        m = Fraction(y2 - y1, x2 - x1)
        b = Fraction(y1*x2 - y2*x1, x2 - x1)

    # the residual intersection of y = mx + b and the line through P and Q
    x3 = m**2 + a1*m - a2 - x1 - x2
    y3 = -1*(m+a1)* x3 - b - a3

    return (x3, y3)

# reference: Silverman AEC III.2.3
# E elliptic curve, P and Q points on E
# return (P*Q) mod p
def ellMultFp(E, P, Q, p):
    if P == "infinity":
        return Q
    if Q == "infinity":
        return P

    # casting coordinates to integers mod p
    x1 = rationaltoFp(Fraction(str(P[0])),p)
    y1 = rationaltoFp(Fraction(str(P[1])),p)

    x2 = rationaltoFp(Fraction(str(Q[0])),p)
    y2 = rationaltoFp(Fraction(str(Q[1])),p)

    a1 = rationaltoFp(Fraction(str(E[0])),p)
    a2 = rationaltoFp(Fraction(str(E[1])),p)
    a3 = rationaltoFp(Fraction(str(E[2])),p)
    a4 = rationaltoFp(Fraction(str(E[3])),p)
    a6 = rationaltoFp(Fraction(str(E[4])),p)

    # if Q = -P, then P + Q = O
    if x1%p == x2%p and (y1 + y2 + a1 * x2 + a3)%p == 0:
        return "infinity"

    # y = mx + b is the line through P and Q

    # if P = Q, take the tangent line at P
    if P == Q:
        m = rationaltoFp(Fraction(3*x1**2 + 2*a2*x1 + a4 - a1*y1, 2*y1 + a1*x1 + a3),p)
        b = rationaltoFp(Fraction(-1*x1**3 + a4*x1 + 2*a6 - a3*y1 , 2*y1 + a1*x1 + a3),p)
    
    # otherwise, point-slope formula does the trick
    else:
        m = rationaltoFp(Fraction(y2 - y1, x2 - x1),p)
        b = rationaltoFp(Fraction(y1*x2 - y2*x1, x2 - x1),p)

    # the residual intersection of y = mx + b and the line through P and Q
    x3 = (m**2 + a1*m - a2 - x1 - x2)%p
    y3 = (-1*(m+a1)* x3 - b - a3)%p

    return (x3, y3)


# P a point defined over Q, p prime
# return the corresponding reduction
def pointModP(P,p):

    if P == "infinity":
        return "infinity"
    
    x = P[0]
    y = P[1]
    
    # if p divides either denominator, then the corresponding Z_p point necessarily reduces to the point at infinity
    if x.denominator % p == 0 or  y.denominator % p == 0:
        return "infinity"

    return (rationaltoFp(x,p), rationaltoFp(y,p))

# s = '[[-3, 0], [-153/7, -64/7]]' 
# -> [[Fraction(-3,1), Fraction(0,1)], [Fraction(-153,7^2), Fraction(-64/7^3)]]
def parseGens(s):
    splits = s.split(',')
    numGens = len(splits)//2
    
    # print('numgens =', numGens)
    temp = []
    for str in splits:
        temp.append(str.strip('[ ]\n'))

    # print('temp =', temp)
    new = []
    for i in range(numGens):
        gen = []
        x = Fraction(Fraction(temp[2*i]).numerator, Fraction(temp[2*i]).denominator**2 )
        y = Fraction(Fraction(temp[2*i+1]).numerator, Fraction(temp[2*i+1]).denominator**3 )
        gen.append(x)
        gen.append(y)
        new.append(gen)
    
    return new

# verifies that a point P is on E
def checkPoint(E,P):
    # casting coordinates to rational numbers 
    x = Fraction(str(P[0]))
    y = Fraction(str(P[1]))

    a1 = Fraction(str(E[0]))
    a2 = Fraction(str(E[1]))
    a3 = Fraction(str(E[2]))
    a4 = Fraction(str(E[3]))
    a6 = Fraction(str(E[4]))

    return y**2 + a1*x*y + a3*y == (x**3 + a2*x**2 + a4*x + a6)


def check(r,p):
    count  = 0
    goodCount = 0
    
    notOnCount = 0
    notOnRedCount = 0

    overlapCount = 0

    # read file
    filestring = "rank" + str(r) + ".txt"
    f = open(filestring, 'r')

    for line in f:
        if line[0] == '"':
            linedata = line.split('\t')
            conductor = int(linedata[1])
            E = eval(linedata[2])
            gens = parseGens(linedata[3])
            
            # if p is a prime of good reduction for the curve, analyze
            if conductor % p != 0:
                
                count+=1
                # get the E(Fp) dictionary
                pts = getFpPoints(E,p)
                N = len(pts)
                
                notOn = False
                for gen in gens:
                    if not checkPoint(E,gen):
                        notOn = True


                # v1: computing powers of MW gen over Q, reducing each point mod p
                # for each MW generator, take N powers and look at images
                # for gen in gens:
                #     P = gen
                #     for i in range(N):
                #         pts[pointModP(P,p)] += 1
                #         P = ellMult(E, P, gen)
                #         if P == "infinity":
                #             break
                
                notOnRed = False
                # v2: reducing MW gen first, then computing powers of MW gen mod p
                for gen in gens:
                    genModP = pointModP(gen,p)
                    P = genModP
                    if P not in pts.keys():
                        notOnRed = True
                        break
                
                if not notOn and not notOnRed:
                    goodCount +=1
                
                if notOn:
                    notOnCount += 1

                if notOnRed:
                    notOnRedCount +=1

                if notOn and notOnRed:
                    overlapCount += 1

                # otherwise, not surjective -> store label
                # else:
                    # notsurj.write(str(N) + "\t" + line)

            if count % 100 == 0:
                print("Progress: ", count, "elliptic curves analyzed", end= "\r")

    print("Done! All elliptic curves in file analyzed.", end='\r')
    print()    

    print("r =", r)
    print("p =", p)
    print("total curves:", count)
    print("good count:", goodCount)
    print("notOnQ count:", notOnCount)
    print("notOnRed count:", notOnRedCount)
    print("================")

    f.close()
    # notsurj.close()
    # broken.close()
    # return(r, p, count, surjcount)
