from random import choice, randrange

f = open("input.txt", 'r', encoding='utf8')
s = f.read()
s = s.replace('\n', ' ')
text = s.split()
words = []
matrix = []

# построение модели

for el in text:
    if el not in words:
        words.append(el)
        matrix.append([])
for i in range(len(matrix)):
    matrix[i] = [0] * len(words)

for i in range(len(text) - 1):
    word_index = words.index(text[i])
    next_word_index = words.index(text[i + 1])
    matrix[word_index][next_word_index] += 1

for i in range(len(matrix)):
    summ = sum(matrix[i])
    if summ:
        for j in range(len(matrix[i])):
            matrix[i][j] /= summ

# генерация текста

k = 100  # количество слов в генерируемом тексте
generated_text = [choice(words)]
for i in range(k):
    num = randrange(1, len(words) + 1)
    last_word_index = words.index(generated_text[-1])
    word_p = matrix[last_word_index][0]
    next_word_index = 0
    while num > word_p * len(words):
        num -= word_p * len(words)
        next_word_index += 1
        print(next_word_index)
        if next_word_index == len(words):
            next_word_index = -1
            break
        word_p = matrix[last_word_index][next_word_index]
    if next_word_index == -1:
        break
    generated_text.append(words[next_word_index])
# print(words)
# print('\n'.join([' '.join(map(str, el)) for el in matrix]))
print(' '.join(generated_text))
