# analyzing the following curve
# "324.a1"	324	1	[]	0	[0, 0, 0, -189, -999]	[[-8, 1]]
# y^2 = x^3 -189x - 999
# E(Q) = Z = <(-8,1)>

from ec import *
from sympy.ntheory import isprime


def check(line):

    writefile = open("newdata/324-a1-pointdicts.txt", "w")

    # primes < 1000 aka first 168 primes
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
              101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
              211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
              307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
              401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
              503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
              601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
              701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
              809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
              907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997
            ]    
    
    surjprimes = []
    notsurjprimes = []
    primeprimes = []
    print(line)

    linedata = line.split('\t')
    conductor = int(linedata[1])
    E = eval(linedata[5])
    gens = parseGens(linedata[6])
    tors = eval(linedata[3])

    # E = [0, 0, 1, -1, 0]
    # conductor = 37
    # gens = [[0,0]]

    indexdict = {}

    for p in primes:
        print("Analyzing p = ",p, end= "\r")
        if conductor % p != 0:

            # get the E(Fp) dictionary
            pts = getFpPoints(E,p)
            N = len(pts)

            # if isprime(N):
            #     allinf = True
            #     for gen in gens:
            #         genModP = pointModP(gen,p)
            #         if genModP != 'infinity':
            #             surjprimes.append(p)
            #             primeprimes.append(p)
            #             allinf = False

            #     if allinf:
            #         print("wow")
            #         notsurjprimes.append(p)

            
            # else:
                # v2: reducing MW gen first, then computing powers of MW gen mod p

            for gen in gens:
                genModP = pointModP(gen,p)
                P = genModP

                for i in range(1,N):
                    if P == "infinity":
                        break
                    pts[P] += 1
                    P = ellMultFp(E, P, genModP,p)

                # if every Fp point has been hit, then all values are > 0



            if not (0 in pts.values()):
                imagesize = N
                
            else:
                imagesize = 0
                for key in pts.keys():
                    if pts[key] > 0:
                        imagesize+= 1
            
            indexdict[p] = N // imagesize
            

            writefile.write(pts)
            writefile.write('\n')
            


    # surjcount = len(surjprimes)
    # notsurjcount = len(notsurjprimes)
    # primecount = len(primeprimes)
    # total = len(primes)


    print("\n")
    
    # print("surj:", surjcount)
    # print("notsurj:", notsurjcount)#, notsurjprimes)
    # print("prime order:", primecount)#,primeprimes)
    # print("surj percentage:", surjcount/total)
    # print("prime order percentage:", primecount/surjcount)
    print(indexdict)
    print("\n")
    
    return(indexdict)


check('"324.a1"	324	1	[]	0	[0, 0, 0, -189, -999]	[[-8, 1]]')