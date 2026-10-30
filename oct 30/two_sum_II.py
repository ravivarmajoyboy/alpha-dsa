total = int(input("Enter number of elements: "))
values = []

for i in range(total):
    x = int(input("Enter number: "))
    values.append(x)

target = int(input("Enter target: "))

start = 0
end = total - 1
answer = False

while start < end:
    current = values[start] + values[end]

    if current == target:
        print("Positions:", start + 1, end + 1)
        answer = True
        break

    elif current < target:
        start += 1

    else:
        end -= 1

if answer == False:
    print("No pair found")