queen = input()
q = [int(i) for i in queen.split(" ")]
bishop = input()
b = [int(i) for i in bishop.split(" ")]

r_q = q[0]
c_q = q[1]
r_b = b[0]
c_b = b[1]

"""bthreat = []
threatrow=[]
threatcol = []

for i in range(8):
    if (i < r_q):
        threatrow.append(r_q - 1)
    else:
        threatrow.append(r_q + 1)
o = []
for i in range(8):
    if (i < r_q):
        threatcol.append(c_q - 1)
    else:
        threatcol.append(c_q + 1)

for k in range(8):
    o[i][j] = o[threatrow[k]][threatcol[k]]

print(k)"""

queenlist = []

#changing column , row is constant
for i in range(1,9):
    queenlist.append((r_q,i))

#changing row , column is constant
for i in range(1,9):
    queenlist.append((i,c_q))

#toplist = []

#recording x wise coordinates
#recording upperside
for i in range(1,(8-(r_q))+1):
    queenlist.append((r_q+i,c_q+i))
    if ((c_q-i)>0):
        queenlist.append((r_q+i,c_q-i))

#recording bottomside
#blist = []
for i in range(1,r_q):
        queenlist.append((r_q-i,c_q+i))
        if (c_q-i > 0):
            queenlist.append((r_q-i,c_q-i)) 
ql = set(queenlist)
queenl = list(ql)
print(queenl)

#recording x wise coordinates - bishop
#recording upperside
bishoplist = []
for i in range((8-(r_b))+1):
    if(r_b+i < 8) and (c_b+i < 8):
        bishoplist.append((r_b+i,c_b+i))
        if ((c_b-i)>0):
            bishoplist.append((r_b+i,c_b-i))

#recording bottomside
for i in range(1,r_b):
        if(r_b+i < 8) and (c_b+i < 8):
            bishoplist.append((r_b-i,c_b+i))
            if (c_b-i > 0):
                bishoplist.append((r_b-i,c_b-i)) 
bl = set(bishoplist)
bishopl = list(bl)
print(bishopl)