first = input("Enter first string: ")
second = input("Enter second string: ")

map1 = {}
map2 = {}
same = True

if len(first) != len(second):
    same = False
else:
    for i in range(len(first)):
        a = first[i]
        b = second[i]

        if a in map1:
            if map1[a] != b:
                same = False
                break
        else:
            map1[a] = b

        if b in map2:
            if map2[b] != a:
                same = False
                break
        else:
            map2[b] = a

print(same)