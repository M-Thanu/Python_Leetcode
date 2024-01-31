import cmath
def quadratic(a,b,c):
    d = (b**2) - (4*a*c)

    sol1=(-b-cmath.sqrt(d))/(2*a)  
    sol2=(-b+cmath.sqrt(d))/(2*a)

    s1=float(abs(sol1))
    s2=float(abs(sol2))

    if s1 > s2:
        bn = s1
        sn = s2
    else:
        bn = s2
        sn = s1

    """print("{:.2f}".format(bn),end=" ")
    print("{:.2f}".format(sn))"""

    return "{:.2f} {:.2f}".format(bn,sn)

while True:
    sinput=input()
    colst=[int(n) for n in sinput.split(" ")]
    p = colst[0]
    q = colst[1]
    r = colst[2]
    if p != 0:
        break    
print(quadratic(p,q,r))