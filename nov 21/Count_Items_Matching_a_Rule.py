
n = int(input("Enter number of items: "))

items = []

for i in range(n):
    item = input("Enter type color name: ")
    parts = item.split(" ")
    items.append(parts)

rule_key = input("Enter rule key: ")
rule_value = input("Enter rule value: ")

if rule_key == "type":
    index = 0
elif rule_key == "color":
    index = 1
else:
    index = 2

count = 0

for i in range(len(items)):
    if items[i][index] == rule_value:
        count = count + 1

print("Output:", count)