def modify_list(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst[i] = lst[i] * lst[i]
        else:
            lst[i] = lst[i] * 3

my_list = [1, 2, 3, 4, 5]
modify_list(my_list)
print(my_list)
