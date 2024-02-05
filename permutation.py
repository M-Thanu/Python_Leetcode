from itertools import permutations 
 
s = input()
 
p = permutations(s) 
lst = []
for j in list(p): 
  lst.append(j)

fset = set(lst)
print(len(fset))