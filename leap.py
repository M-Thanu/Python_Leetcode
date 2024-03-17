year = int(input())
if year % 100 == 0:
    if (year // 4) & (year // 400):
        print("leap year")
    else:
        print("not a leap year")
elif year % 4 == 0 :
    print("leap year")
else:
    print("not a leap year")
