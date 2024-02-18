def classify_triangle(points):
    ms = 0

    #calculating length of three sides using vertices
    a = ((vl[0][0] - vl[1][0])**2 + (vl[0][1] - vl[1][1])**2)** 0.5
    b = ((vl[1][0] - vl[2][0])**2 + (vl[1][1] - vl[2][1])**2)** 0.5
    c = ((vl[0][0] - vl[2][0])**2 + (vl[0][1] - vl[2][1])**2)** 0.5

    A = round(abs(a)) 
    B = round(abs(b)) 
    C = round(abs(c)) 

    #finding the biggest side
    if A > B:
        if A > C:
            ms = A
        else :
            ms = C
    elif B > C :
        ms = B
    else:
        ms = C

    #defining finding biggest and smallest sides
    sl = [A, B, C]
    othersides=[]
    for i in sl:
        if i == ms:
            continue
        else:
            othersides.append(i)

    #implementing the logic
    if ((ms)**2 > (othersides[0]**2 + othersides[1]**2)): 
        print("Obtuse")
    elif((ms)**2 == (othersides[0]**2 + othersides[1]**2)):
        print("Right Angled")
    elif((ms)**2 < (othersides[0]**2 + othersides[1]**2)):
        print("Acute")
    else:
        print("Check your input")

#getting input and storing as a list
Lin=input()
Lc = Lin[2:-2]
Lrow = Lc.split("),(")
vl = [[int(n) for n in vlist.split(",")] for vlist in Lrow]
classify_triangle(vl)
