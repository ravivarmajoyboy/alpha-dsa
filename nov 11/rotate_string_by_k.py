text = input("Enter a string: ")
k = int(input("Enter rotation count: "))

n = len(text)

if n > 0:
    k = k % n

answer = [""] * n

for i in range(n):
    new_index = (i + k) % n
    answer[new_index] = text[i]

result = ""

for ch in answer:
    result = result + ch

print("Output:", result)