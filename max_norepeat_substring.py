# 最大不重复字符的子串

def max_norepeat_substring(s):
    i, j =0, 0
    d = set()
    length = len(s)
    while i<length and j < length:
        print(d)
        while s[j] not in d:
            d = d | {s[j]}
            j += 1
        while s[i] in d:
            d = d - {s[i]}
            i += 1

        answer = j -i
        print(answer)
s = 'fewfeiwjfoaifjewofewfewa'
print(max_norepeat_substring(s))