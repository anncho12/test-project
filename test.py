import sys

S=sys.stdin.readline().rstrip()
l=len(S)
s=set()
for i in range(l):
    for j in range(i+1, l+1):
        s.add(S[i:j])
print(len(s))