userin = input()
fset = set(userin)
print(fset)
fl=[]
for i in range(len(userin)):
    for j in range((i)):
        if (userin[i] == userin[j]):
            break
        else:
            fl.append(userin[i])
print(len(f1))
