word = input().upper()
word_list = (list(set(word)))
print(word_list)
cnt = []

for i in word_list:
    cnt.append(word.count(i))

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(word_list[(cnt.index(max(cnt)))]) 

# for i in range(len(alphabet)):
#     if max(alphabet[i]):
#         print(" ",max(alphabet[i]))