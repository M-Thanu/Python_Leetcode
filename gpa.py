tcr = 0
ts1 = 0
while True :
    cr = int (input("Enter Credit: "))
    if cr == 0 :
        break
    gpa = int(input("Enter GPA: "))

    tcr = tcr + cr
    s1 = cr * gpa
    ts1 = ts1 + s1

agpa = ts1 / tcr

print(agpa)

    