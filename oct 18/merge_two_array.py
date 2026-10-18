n = int(input("Enter size of first array: "))
a = []

for i in range(n):
    a.append(int(input()))

m = int(input("Enter size of second array: "))
b = []

for i in range(m):
    b.append(int(input()))

i = 0
j = 0
result = []

while i < n and j < m:
    if a[i] <= b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1

while i < n:
    result.append(a[i])
    i += 1

while j < m:
    result.append(b[j])
    j += 1

print(result)