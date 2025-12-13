from ec import *
from sympy.ntheory import isprime


# get data for rank r, prime p
# how many curves have cyclic vs noncyclic E(F_p)
def gather(r, p):
    count  = 0
    cycliccount = 0
    
    # read file
    filestring = "lmfdb/rank" + str(r) + ".txt" # checking all rank r ell curves
    # filestring = "rank" + str(r) + "mod" + str(p) + "notsurjlabels.txt" # checking the ell curves that do not surject onto the image
    f = open(filestring, 'r')
    
    for line in f:
        if line[0] == '"':
            linedata = line.split('\t')
            conductor = int(linedata[1])
            E = eval(linedata[2])
            gens = parseGens(linedata[3])

            # if p is a prime of good reduction for the curve, analyze
            if conductor % p != 0:

                # get #E(F_p)
                pts = getFpPoints(E,p)
                N = len(getFpPoints(E,p))

                # if N is 1 or prime, then E(F_p) is necessarily cyclic
                # if N == 1 or isprime(N):
                
                notcyclic = True
                
                if N == 1 or isprime(N):
                    cycliccount += 1

                else:
                    # reduce MW gen first, then computing powers of MW gen mod p
                    for gen in pts:
                        genModP = pointModP(gen,p)
                        P = genModP

                        # e.g. N = 6
                        # i = 1: P \neq O
                        # i = 2: P^2 \neq O
                        # i = 5: P^2


                        # This is bad: requires the MW gen to reduce to the generator (effectively saying cyclic iff surjective)


                        # check if gen^{i} = 0
                        for i in range(1, N):
                            if P == "infinity":
                                break
                            
                            if i == N-1: # if P has N-1 nontrivial powers, then it is necessarily a generator for all E(F_p)
                                cycliccount += 1
                                notcyclic = False

                            # compute P^{i+1}
                            P = ellMultFp(E, P, genModP,p)
                            
                        if not notcyclic:
                            break

                count += 1

            if count % 100 == 0:
                print("Progress: ", count, "elliptic curves analyzed", end= "\r")

    print("Done! All elliptic curves in file analyzed.", end='\r')
    print()    

    print("r =", r)
    print("p =", p)
    print("total curves:", count)
    print("cyclic count:", cycliccount)
    print("percentage:", cycliccount/count)
    print("================")

    f.close()
    # notsurj.close()
    # broken.close()
    return(r, p, count, cycliccount)

# gather data across all ranks and a specified set of primes
def main():
    globalfile = open("newdata/totalcyclicdata.txt", "w")
    
    primes = [2,3,5,7,11,13]
    # for each rank
    # for r in range(1,2):
    r=1
    for p in primes:
        (r,p,count,cycliccount) = gather(r,p)
        globalfile.write(str(r) + ", " + str(p)  + ", " + str(count)  + ", " + str(cycliccount) + ',' + str(cycliccount/count) + "\n")

    globalfile.close()


if __name__ == "__main__":
    main()