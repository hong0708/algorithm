def solution(s):
    answer = 0
    imp_word = ''
    imp_list = []
    imp_count = 0
    for i in range(len(s)):
        if len(imp_list) == 0:
            imp_word = s[i]
            imp_count += 1
            imp_list.append(s[i])
        else:
            if s[i] == imp_word:
                imp_list.append(s[i])
                imp_count += 1
            else:
                imp_list.append(s[i])
                if len(imp_list) == imp_count * 2:
                    answer += 1
                    imp_word = ''
                    imp_list = []
                    imp_count = 0
    if len(imp_list) > 0:
        answer += 1
    return answer


print(solution("abracadabra"))
