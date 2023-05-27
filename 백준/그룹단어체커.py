N = int(input())
answer = 0
for _ in range(N):
    word = input()
    impl = []
    is_right = True
    for j in range(len(word)):
        if word[j] in impl and impl[-1] != word[j]:
            is_right = False
            break
        else:
            impl.append(word[j])
    if is_right:
        answer += 1
print(answer)
