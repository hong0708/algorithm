import sys

S = sys.stdin.read()

print(S)

cnt = [0] * 26
for s in S:
    if s.islower():
        cnt[ord(s) - ord('a')] += 1

max_word = max(cnt)
result = ''
for i in range(len(cnt)):
    if cnt[i] == max_word:
        result += chr(i + ord('a'))
print(result)