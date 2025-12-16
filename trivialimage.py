# if E(Q) -> E(F_p) is not surjective, what is the size of the image?

from ec import *


# get data for rank r, prime p
def gather(r, p):
    count  = 0
    trivcount = 0
    
    # read file
    # filestring = "lmfdb/rank" + str(r) + ".txt"
    filestring = "newdata/rank" + str(r) + "mod"+ str(p) + "notsurjlabels.txt"
    f = open(filestring, 'r')
    
    # write file
    # notsurj = open("newdata/rank" + str(r) + "mod"+ str(p) + "notsurjlabels.txt", 'w')

    for line in f:
        if line[0] == '"':
            linedata = line.split('\t')
            conductor = int(linedata[1])
            E = eval(linedata[2])
            gens = parseGens(linedata[3])

            # if p is a prime of good reduction for the curve, analyze
            if conductor % p != 0:

                # get the E(Fp) dictionary
                pts = getFpPoints(E,p)
                N = len(pts)

                # v1: computing powers of MW gen over Q, reducing each point mod p
                # for each MW generator, take N powers and look at images
                # for gen in gens:
                #     P = gen
                #     for i in range(N):
                #         pts[pointModP(P,p)] += 1
                #         P = ellMult(E, P, gen)
                #         if P == "infinity":
                #             break
                

                # v2: reducing MW gen first, then computing powers of MW gen mod p
                for gen in gens:
                    genModP = pointModP(gen,p)
                    P = genModP

                    for i in range(1,N):
                        if P == "infinity":
                            break
                        pts[P] += 1
                        P = ellMultFp(E, P, genModP,p)



                count += 1

                # if every Fp point has been hit, then all values are > 0
                if not (0 in pts.values()):
                    imagesize = N
                
                else:
                    imagesize = 0
                    for key in pts.keys():
                        if pts[key] > 0:
                            imagesize+= 1
                
                if imagesize == 1:
                    trivcount += 1
            


            if count % 100 == 0:
                print("Progress: ", count, "elliptic curves analyzed", end= "\r")

    print("Done! All elliptic curves in file analyzed.", end='\r')
    print()    

    print("r =", r)
    print("p =", p)
    print("total curves:", count)
    print("trivial reduction count:", trivcount)
    print("percentage:", trivcount/count)
    print("================")

    f.close()
    # notsurj.close()
    # broken.close()
    return(r, p, count, trivcount)

# gather data across all ranks and a specified set of primes
def main():
    globalfile = open("newdata/totaltrivdata.txt", "w")
    
    primes = [2,3,5,7,11,13,101]
    # for r = 1 for now
    for r in range(1,2):

        for p in primes:
            (r,p,count,trivcount) = gather(r,p)
            globalfile.write(str(r) + ", " + str(p)  + ", " + str(count)  + ", " + str(trivcount) + ',' + str(trivcount/count) + "\n")

    globalfile.close()


if __name__ == "__main__":
    main()



##### Testing

# e.g. https://www.lmfdb.org/EllipticCurve/Q/5077/a/1 -> E = [0, 0, 1, -7, 6]
# y^2 + y = x^3 - 7x + 6$
# print(getFpPoints([0, 0, 1, -7, 6], 3))

# print(getFpPoints([0, 0, 1, -7, 6], 2))
# print(getFpPoints([0, 0, 1, -7, 6], 5))
# print(getFpPoints([0, 0, 1, -7, 6], 7))




# y^2 + y = x^3 - x^2 - 10 x - 20
# E = [0, -1, 1, -10, -20]
# p = 7
# print(getFpPoints(E,p))

# P = (5,5)
# P2 = ellMult(E, P, P)
# P3 = ellMult(E, P2, P)
# P4 = ellMult(E, P3, P)
# P5 = ellMult(E, P4, P)

# print("P =", P)
# print("P2 =", P2)
# print("P3 =", P3)
# print("P4 =", P4)
# print("P5 =", P5)


# print(v(2**8*3**5, 5))

# E = [0, 0, 0, -53787, -10435066]

# P = (379,4860)
# Pi = P
# print("P =", P)
# for i in range(2,25):
#     Pi = ellMult(E,P,Pi)
#     print("P^", i, " =", Pi)

# print(pointModP((5,5),7))
# print(pointModP((Fraction(1,5),Fraction(1,5)),5))


# LMFDB data
# label | conductor | 


# iterate through LMFDB entries
# if conductor % p != 0:
#   get Fp points
#   take MW gen and multiples, reduce each mod p and see if all points are hit
#   if all hit, mark surjective
#   otherwise try other mw gens

# check(1,3)
# print(gather(4,3))
# s= '[[-3, 0], [-153/7, -64/7]]'
# print(parseGens(s))

# s= '[[-3, 0], [-153/7, -64/7]]'
# print(parseGens(s))