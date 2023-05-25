def sol():
    word = input()
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - 1 - i]:
            return 0
    return 1


print(sol())
