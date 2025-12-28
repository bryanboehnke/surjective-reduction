# if E(Q) -> E(F_p) is not surjective, what is the size of the image?

from ec import *


# get data for rank r, prime p
def gather(r, p):
    count  = 0
    avgindex = 0
    
    # read file
    filestring = "lmfdb/rank" + str(r) + ".txt"
    # filestring = "newdata/rank" + str(r) + "mod"+ str(p) + "notsurjlabels.txt"
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
                
                # first, check that index is indeed integral
                if N % imagesize == 0:
                    avgindex = (avgindex * (count - 1) + (N / imagesize) ) / count
            


            if count % 100 == 0:
                print("Progress: ", count, "elliptic curves analyzed", end= "\r")

    print("Done! All elliptic curves in file analyzed.", end='\r')
    print()    

    print("r =", r)
    print("p =", p)
    print("total curves:", count)
    print("average index:", avgindex)
    # print("percentage:", avgindex/count)
    print("================")

    f.close()
    # notsurj.close()
    # broken.close()
    return(r, p, count, avgindex)

# gather data across all ranks and a specified set of primes
def main():
    globalfile = open("newdata/avgindexdata.txt", "w")
    
    primes = [2,3,5,7,11,13,101]
    # for r = 1 for now
    for r in range(1,2):

        for p in primes:
            (r,p,count,avg) = gather(r,p)
            globalfile.write(str(r) + ", " + str(p)  + ", " + str(count)  + ", " + str(avg) + "\n")

    globalfile.close()


if __name__ == "__main__":
    main()


