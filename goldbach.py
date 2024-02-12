def is_goldbach(user):
    prime = False

    for i in range(1,userin+1):
        if (userin == (i + i)):
            for j in range(2,i):
                if i % j != 0:
                    prime = True               
    if prime:
        print("Goldbach's conjecture is sastisfied")
    else :
        print("Goldbach’s conjecture cannot be applied")

userin = int(input())
is_goldbach(userin)
