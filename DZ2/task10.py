s = input()
glasnie = 'уеёыаоэяиюэ'
zvuk_to_bukva = {'у': 'у', 'е': 'е', 'ё': 'ё', 'ы': 'ы', 'а': 'а', 'о': 'о', 'э': 'э', 'я': 'а', 'и': 'и', 'ю': 'у'}
s2 = s[0]
for i in range(1, len(s)):
    s2 += s[i]
    if s[i] in glasnie and s[i - 1] not in glasnie + ' ':
        s2 += 'с' + zvuk_to_bukva[s[i]]
print(s2)
