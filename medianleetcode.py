userin1 = input() 
l1 = [int(i) for i in userin1.split(",")]
userin2 = input()
l2 = [int(i) for i in userin2.split(",")]

for j in range(len(l2)):
    l1.append(l2[j])
l1.sort()

if len(l1) % 2 == 1:
    median = l1[len(l1) // 2]

else :
    median = (l1[((len(l1) // 2) - 1)] + l1[(len(l1) // 2)]) / 2

print(median)
