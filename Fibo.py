flst=[0,1]
for i in range(0,1000):
    element=flst[i]+flst[i+1]
    flst.append(element)

a = int(input())
b = int(input())
sum = 0

for k in range(a-1 , b):
    sum = sum + flst[k]

print(sum)  
