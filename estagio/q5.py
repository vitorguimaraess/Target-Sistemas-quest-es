def inverte(s):
    temp = ''
    for i in range(len(s)):
        temp += s[-(i+1)]
    return temp

print(inverte(input()))
