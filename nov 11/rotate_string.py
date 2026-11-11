word = input("Enter the original string: ")
goal = input("Enter the goal string: ")

found = False

if len(word) == len(goal):
    n = len(word)

    for start in range(n):
        same = True

        for j in range(n):
            pos = (start + j) % n

            if word[pos] != goal[j]:
                same = False
                break

        if same:
            found = True
            break

print(found)