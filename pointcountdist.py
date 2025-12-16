# gather point counts across ranks
def compile():
    pointcounts = open("newdata/totalsizedata.txt", "r")
    data = pointcounts.readlines()
    pointcounts.close()

    compiledcounts = open("newdata/compiledpointcounts.csv", "w")

    # for each prime, gather all data
    for p in [2,3,5,7,11,13,101]:
        primedict = {}
        for line in data:
            linedata = line.split("\t")
            prime = eval(linedata[1])
            tempdict = eval(linedata[2])
            
            # print(p, prime)
            # if we are at the right prime, add the dict values to the primedict
            if prime == p:

                if primedict == {}:
                    primedict = tempdict
                else:
                    for key in tempdict.keys():
                        primedict[key] += tempdict[key]

        
        compiledcounts.write("F_"+str(p)+"\n")
        for key in primedict.keys():
            compiledcounts.write(str(key) + "," + str(primedict[key]) + "\n")    

        
    
    
    compiledcounts.close()




if __name__ == "__main__":
    compile()