s = "aabcddddefgg"

result = []

pre_word = ""
add_word = ""

for i in range(len(s)):
    if i == 0:
        pre_word = s[i]
    else:
        if i == len(s) - 1:
            if s[i] == pre_word:
                add_word += "0"
            else:
                add_word += s[i]
            break

        if pre_word == s[i]:
            add_word += "0"

        elif pre_word != s[i]:
            add_word += pre_word
            pre_word = s[i]

print(add_word)