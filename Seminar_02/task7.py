a = input().split()
max_k = 0
elem_max_k = []
for el in a:
    k = a.count(el)
    if k > max_k:
        max_k = k
        elem_max_k = [el]
    elif k == max_k and el not in elem_max_k:
        elem_max_k.append(el)
print(' '.join(elem_max_k))
