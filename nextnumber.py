def next_high_num(a):
    nlist = a[0:-2]
    numlist = list(nlist)

    if (a[-1] > a[-2]):
        numlist.append(a[-1])
        numlist.append(a[-2])
        print(int(''.join(map(str, numlist))))

    else:
        print("Not Possible")

num = str(input())
next_high_num(num)
