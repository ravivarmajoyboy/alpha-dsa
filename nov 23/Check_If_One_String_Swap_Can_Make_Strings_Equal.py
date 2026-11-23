
first = input("Enter first string: ")
second = input("Enter second string: ")

answer = False

if len(first) == len(second):

    if first == second:
        answer = True

    else:
        pos = []

        for i in range(len(first)):
            if first[i] != second[i]:
                pos.append(i)

        if len(pos) == 2:
            a = pos[0]
            b = pos[1]

            if first[a] == second[b] and first[b] == second[a]:
                answer = True

print("Output:", answer)