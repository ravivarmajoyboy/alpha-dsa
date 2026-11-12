n = int(input("Enter a number: "))

num = "1"

for i in range(n - 1):
    result = ""
    count = 1

    for j in range(len(num)):
        if j < len(num) - 1 and num[j] == num[j + 1]:
            count += 1
        else:
            result += str(count) + num[j]
            count = 1

    num = result

print("Count and Say:", num)