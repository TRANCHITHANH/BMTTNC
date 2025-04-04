from itertools import permutations
lst = [1, 2, 3]
perms = list(permutations(lst))
print("Tất cả các hoán vị của [1, 2, 3]:")
for p in perms:
    print(p)
