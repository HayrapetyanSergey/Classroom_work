word = None
ans = []
while word != ' ':
    word = input("Enter words: ")
    if word not in ans:
        ans.append(word)
del ans[-1]
print(ans)
