def reversed_word(word):
    res = ""
    for i in range(len(word) - 1, -1, -1):
        res += word[i]
    return res

word = input("Enter word: ")
print(reversed_word(word))
