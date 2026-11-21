
first = input("Enter first string: ")
second = input("Enter second string: ")

answer = False

if len(first) == len(second):

    if first == second:
        seen = []

        for ch in first:
            if ch in seen:
                answer = True
                break
            else:
                seen.append(ch)

    else:
        positions = []

        for i in range(len(first)):
            if first[i] != second[i]:
                positions.append(i)

        if len(positions) == 2:
            a = positions[0]
            b = positions[1]

            if first[a] == second[b] and first[b] == second[a]:
                answer = True

print("Output:", answer)