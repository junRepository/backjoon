h, m, s = map(int, input().split())
d = int(input())

s1 = (s+d)%60
m1 = (s+d)//60

m2 = (m+m1)%60
h1 = (m+m1)//60

h2 = (h+h1)%24
print(h2, m2, s1)
