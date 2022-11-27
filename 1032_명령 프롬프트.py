N = int(input())
word = list(input())
word_len = len(word)

for i in range(N-1):
    other_word = list(input())
    for j in range(word_len):
        if word[j] != other_word[j]:
            word[j] = '?'

print(' '.join(word),end = '')
