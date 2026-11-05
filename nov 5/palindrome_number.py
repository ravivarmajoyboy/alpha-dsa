number = int(input("Enter a number: "))

original_num = number
rev = 0

if number < 0:
    print("Not Palindrome")
else:
    while number > 0:
        last_digit = number % 10
        rev = rev * 10 + last_digit
        number = number // 10

    if original_num == rev:
        print("Palindrome Number")
    else:
        print("Not Palindrome")