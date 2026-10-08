import string

f = open('task7_input.txt', 'r', encoding='utf8')

data = f.read()
for s in string.punctuation:
    data = data.replace(s, '')
data = data.replace('\n', ' ')
words = list(map(lambda x: str(x).lower(), data.split()))
word_dict = {}
for el in words:
    if el not in word_dict:
        word_dict[el] = 1
    else:
        word_dict[el] += 1
maxx = []
maxx_word = ''
while len(maxx) < 10 and len(maxx) < len(word_dict.keys()):
    maxx_num = 0
    for key in word_dict:
        if len(maxx) == 0:
            if word_dict[key] > maxx_num:
                maxx_num = word_dict[key]
                maxx_word = key
        else:
            if maxx[-1][0] > word_dict[key] > maxx_num:
                maxx_num = word_dict[key]
                maxx_word = key
    maxx.append((maxx_num, maxx_word))
print('Десять самых часто употребяемых слов:')
k = 1
for el in maxx:
    print(f'{k}) {el[1]} - {el[0]}')
    k += 1
