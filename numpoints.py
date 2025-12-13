from ec import *
import os.path

# get data for rank r, prime p
# what are the sizes of E(F_p)?
def gather(r, p):
    count  = 0
    sizes = {}
    
    # read file

    # curpath = os.path.dirname(__file__)
    # newpath = os.path.relpath("\\lmfdb\\rank" + str(r) + ".txt", curpath)

    filestring = "lmfdb/rank" + str(r) + ".txt" # checking all rank r ell curves
    # filestring = "rank" + str(r) + "mod" + str(p) + "notsurjlabels.txt" # checking the ell curves that do not surject onto the image
    f = open(filestring, 'r')
    
    # write file
    # weird = open("rank" + str(r) + "mod"+ str(p) + "weirdcycliclabels.txt", 'w')

    for line in f:
        if line[0] == '"':
            linedata = line.split('\t')
            conductor = int(linedata[1])
            E = eval(linedata[2])
            # gens = parseGens(linedata[3])

            # if p is a prime of good reduction for the curve, analyze
            if conductor % p != 0:

                # get #E(F_p)
                N = len(getFpPoints(E,p))

                if N in sizes.keys():
                    sizes[N] += 1
                else:
                    sizes[N] = 1


                count += 1

            if count % 100 == 0:
                print("Progress: ", count, "elliptic curves analyzed", end= "\r")

    print("Done! All elliptic curves in file analyzed.", end='\r')
    print()    

    print("r =", r)
    print("p =", p)
    print("total curves:", count)
    print("================")

    f.close()
    # notsurj.close()
    # broken.close()
    return(r, p, sizes)

# gather data across all ranks and a specified set of primes
def main():

    globalfile = open('newdata/totalsize.txt', "w")
    
    primes = [2,3,5,7,11,13, 101]
    # for each rank
    for r in range(1,6):
    # r=1
        for p in primes:
            (r,p,sizes) = gather(r,p)
            globalfile.write(str(r) + ", " + str(p)  + ", " + str(sizes) + "\n")

    globalfile.close()


if __name__ == "__main__":
    main()