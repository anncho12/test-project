import sys

N=int(sys.stdin.readline())
cost=[]
for _ in range(N):
    cost=cost+list(map(int, sys.stdin.readline().split()))
print(cost)
color=[0]*N
sum_cost=[0]*N
for i in range(N):
    