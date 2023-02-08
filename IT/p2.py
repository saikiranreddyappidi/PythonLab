from itertools import combinations

arr=list(map(int,input().split()))
k=int(input())
l=len(arr)
comb=list(combinations(arr,k))
print(comb)