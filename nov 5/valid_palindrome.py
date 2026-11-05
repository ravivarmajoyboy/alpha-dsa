name = input("Enter a string: ")

start = 0
end = len(name) - 1
same = True

while start < end:

    if not (('a' <= name[start] <= 'z') or
            ('A' <= name[start] <= 'Z') or
            ('0' <= name[start] <= '9')):
        start += 1

    elif not (('a' <= name[end] <= 'z') or
              ('A' <= name[end] <= 'Z') or
              ('0' <= name[end] <= '9')):
        end -= 1

    else:
        first = name[start]
        last = name[end]

        if 'A' <= first <= 'Z':
            first = chr(ord(first) + 32)

        if 'A' <= last <= 'Z':
            last = chr(ord(last) + 32)

        if first != last:
            same = False
            break

        start += 1
        end -= 1

if same:
    print("Palindrome")
else:
    print("Not Palindrome")