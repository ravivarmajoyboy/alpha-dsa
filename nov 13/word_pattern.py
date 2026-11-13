pattern = input("Enter pattern: ")
sentence = input("Enter words: ")

words = sentence.split(" ")

char_map = {}
word_map = {}
answer = True

if len(pattern) != len(words):
    answer = False
else:
    for i in range(len(pattern)):
        ch = pattern[i]
        word = words[i]

        if ch in char_map:
            if char_map[ch] != word:
                answer = False
                break
        else:
            char_map[ch] = word

        if word in word_map:
            if word_map[word] != ch:
                answer = False
                break
        else:
            word_map[word] = ch

print(answer)