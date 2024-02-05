s = input()
l1 = [i for i in s]
l2 = []
a = len(l1)

for j in range(0,a-1):
    if (l1[j] == l1[j+1]):
        continue
    elif (l1[j] != l1[j-1]):
        l2.append(l1[j-1])
        l2.append(l1[j])
        l2.append(l1[j+1])

fset = set(l2)
print(len(fset))

"""a b b c d 
a a b c c d 
test case 03:a a b c d d e
test case 04 : """
