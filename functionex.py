def printSum(k):
    if k>0:
        return k + printSum(k-1)
    else:
        return 0

result = 5
print(printSum(result))