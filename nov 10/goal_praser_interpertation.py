command = input("Enter the command: ")

result = ""
i = 0

while i < len(command):

    if command[i] == "G":
        result = result + "G"
        i = i + 1

    elif command[i] == "(" and command[i + 1] == ")":
        result = result + "o"
        i = i + 2

    else:
        result = result + "al"
        i = i + 4

print("Output:", result)