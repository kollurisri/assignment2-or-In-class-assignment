def unique_list(l):
    u = []
    for i in l:
        if i not in u:
            u.append(i)
    return u
print(unique_list([1,2,3,3,3,3,4,5]))
