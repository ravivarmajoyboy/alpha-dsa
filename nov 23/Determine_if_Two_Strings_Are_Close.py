
word1 = input("Enter first string: ")
word2 = input("Enter second string: ")

answer = True

if len(word1) != len(word2):
    answer = False
else:
    count1 = {}
    count2 = {}

    for ch in word1:
        if ch in count1:
            count1[ch] = count1[ch] + 1
        else:
            count1[ch] = 1

    for ch in word2:
        if ch in count2:
            count2[ch] = count2[ch] + 1
        else:
            count2[ch] = 1

    for ch in count1:
        if ch not in count2:
            answer = False
            break

    if answer:
        freq1 = []
        freq2 = []

        for ch in count1:
            freq1.append(count1[ch])

        for ch in count2:
            freq2.append(count2[ch])

        # Manual bubble sort
        for i in range(len(freq1)):
            for j in range(len(freq1) - i - 1):
                if freq1[j] > freq1[j + 1]:
                    temp = freq1[j]
                    freq1[j] = freq1[j + 1]
                    freq1[j + 1] = temp

        for i in range(len(freq2)):
            for j in range(len(freq2) - i - 1):
                if freq2[j] > freq2[j + 1]:
                    temp = freq2[j]
                    freq2[j] = freq2[j + 1]
                    freq2[j + 1] = temp

        for i in range(len(freq1)):
            if freq1[i] != freq2[i]:
                answer = False
                break

print("Output:", answer)