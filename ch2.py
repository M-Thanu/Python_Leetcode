def find_prime_numbers(a):
    for i in range(2,a):
        for j in range(2,i):
            if (i % j == 0):
                break
            if(i % 2 == 0):
                continue
        else:
            print(i, end=' ')
                
n = int(input())
find_prime_numbers(n)


l1=input()
nums=[int(n) for n in l1.split(",")]
target = int(input())
for i in nums:
    for j in range(1,len(nums)):
        if((i+nums[j])==target):
            a = nums.index(i)
            b = j
l2=[]
l2.append(a)
l2.append(b)
print(l2)

