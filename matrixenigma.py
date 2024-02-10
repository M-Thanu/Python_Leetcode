Ain = input()
Ac = Ain[2:-2]
Arow = Ac.split("], [")
A = [[int(n) for n in Alist.split(",")] for Alist in Arow]

"""
A = [[1,2,3], [4,5,6]]
B = [[7,8], [9,10], [11,12]]
"""
Bin = input()
Bc = Bin[2:-2]
Brow = Bc.split("], [")
B = [[int(n) for n in Blist.split(",")] for Blist in Brow]

m = len(A)
p = len(B)
n = len(A[0])
q = len(B[0])

if n == p:
    f = [[0 for _ in range(q)] for _ in range(m)]
    for i in range(m):
        for j in range(q):
            for k in range(n):
                f[i][j] = f[i][j] + A[i][k] * B[k][j]
    print(f)

elif len(A[0]) != len(A[1]):
    print("A is an invalid matrix. Number of elements in rows are not equal")

else :
    print("Incompatible matrices for multiplication. Number of columns in A must be equal to the number of rows in B.")
                
