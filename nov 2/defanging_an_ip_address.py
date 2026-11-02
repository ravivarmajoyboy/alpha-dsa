ip = input("Enter IP address: ")

result = []

for ch in ip:
    if ch == ".":
        result.append("[.]")
    else:
        result.append(ch)

final_ip = "".join(result)

print("Defanged IP:", final_ip)