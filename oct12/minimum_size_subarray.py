n = int(input("enter the total number: "))
a = []
for i in range(n):
    a.append(int(input("enter the number: ")))
t = int(input("enter the target: "))

small = n + 1
i = 0
j = 0
s = 0

while j < n:
    s = s + a[j]
    j = j + 1
    while s >= t:
        if j - i < small:
            small = j - i
        s = s - a[i]
        i = i + 1

if small == n + 1:
    print(0)
else:
    print(small)