#입력 받은 알파벳을 대문자(.upper())로 저장
word = input().upper()
#중복되는 입력 제외하고 리스트에 저장
word_list = (list(set(word)))
#카운트를 저장할 리스트 초기화
cnt = []

for i in word_list:
    #word_list에 저장된 alphabet 사용된 횟수 cnt에 저장
    cnt.append(word.count(i))
#가장 많이 사용된 alphabet이 여러개 존재할 경우 ?를 출력 
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(word_list[(cnt.index(max(cnt)))]) 