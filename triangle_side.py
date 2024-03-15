nums = input()
Nc = nums[1:-1]
slist = [int(n) for n in Nc.split(",")]
side = set(slist)

if len(side) == 1:
    print("equilateral")

elif len(side) == 2:
    print("isosceles")

else:
    print("scalene")