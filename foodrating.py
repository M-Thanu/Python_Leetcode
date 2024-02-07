userin = eval(input())
food = userin[0]
cuisine = userin[1]
rating = userin[2]

c1=[]
r1=[]

a = input()

if a == "highestRated":
    b = input()
    for i in range(0,len(cuisine)):
        if b == cuisine[i] :
            c1.append(i)
    for j in range(0,len(c1)):
        r1.append(rating[c1[j]])

    maxrated = max(r1)
    foodindex = rating.index(maxrated)
    print(food[foodindex])

else :
    c = input()
    changelist = [k for k in c.split(" ")]
    print(changelist)
    for k in range(0,len(food)):
        if food[k] == changelist[0] :
            rating[k] = int(changelist[1])
print(food)
print(rating)