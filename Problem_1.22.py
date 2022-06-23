def vowel(n:str):
    if n == 'a' or n == 'i' or  n == 'o' or n == 'u' or n == 'e':
        return f"{n} is vowel"
    elif n == 'y':
        return f"{n} can be vowel or consonant"
    return f"{n} is consonant"

word = str(input())
print(vowel(word))