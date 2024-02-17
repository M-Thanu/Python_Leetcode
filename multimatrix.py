u1 = input()
ulist = [int(n) for n in u1.split(" ")]
m = ulist[0]
n = ulist[1]
Alist = []
A = []
for i in range(m):
    Arow = input()
    Alist = [int(n) for n in Arow.split(" ")]
    A.append(Alist)

u2 = input()
u2list = [int(n) for n in u2.split(" ")]
p = u2list[0]
q = u2list[1]
Blist = []
B = []
for i in range(p):
    Brow = input()
    Blist = [int(n) for n in Brow.split(" ")]
    B.append(Blist)

if n == p:
    f = [[0 for _ in range(q)] for _ in range(m)]
    for i in range(m):
        for j in range(q):
            for k in range(n):
                f[i][j] = f[i][j] + A[i][k] * B[k][j]
    num_row = len(f)
    for s in range(num_row):
        result = ' '.join(map(str, f[s]))
        print(result)

elif (n != len(Arow)) or (q != len(Brow)):
    print("Invalid input. Ensure correct number of values.")

elif (n != p):
    print("Matrix multiplication is not possible due to dimension mismatch.")

else:
    print("Invalid input. Values are not numeric.")
   