l1=input()
l1 = [int(n) for n in l1.split(",")]

l2 = input()
l2 = [int(i) for i in l2.split(",")]

l1.reverse()
l2.reverse()

s1=[str(j) for j in l1]
fs1="".join(s1)

s2=[str(k) for k in l2]
fs2="".join(s2)

f_out=int(fs1) + int(fs2)
final = str(f_out)
rest = final[::-1]

ol=[]
for l in rest:
    ol.append(int(l))

print(ol)
