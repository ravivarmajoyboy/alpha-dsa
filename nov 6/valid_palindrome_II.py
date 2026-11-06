s = input("Enter string: ")

i = 0
j = len(s) - 1
flag = True

while i < j:
    if s[i] == s[j]:
        i += 1
        j -= 1
    else:
        a = i + 1
        b = j

        while a < b and s[a] == s[b]:
            a += 1
            b -= 1

        if a >= b:
            flag = True
        else:
            a = i
            b = j - 1

            while a < b and s[a] == s[b]:
                a += 1
                b -= 1

            if a >= b:
                flag = True
            else:
                flag = False

        break

if flag:
    print("True")
else:
    print("False")