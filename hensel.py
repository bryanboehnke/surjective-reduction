# given f(x) with a simple root t in F_p, lift to a root in Z_p to a given amount of precision

# monic cubic poly for now
# f(x) = x^3 + a1 x^2 + a2 x + a3

# e.g. f(x) = x^3 + x + 1
f = [0,1,1]
p = 11

# root of f(x) in F_p
tbar = 2

# lift to (an approximation of) a root t in Z_p
t = [tbar]

# degree of precision
ntop = 10


for n in range(1,ntop):
    z = 0

    for k in range(len(t)):
        z += t[k]* p**k

    # get z expansion from list

    for a in range(p):
        x = (z+ a*p**(n))
        # if f(x) = 0
        if (x**3 + f[0]*x**2 + f[1]*x + f[2]) % p**(n+1) == 0: 
            t.append(a)
            break

print(t)


