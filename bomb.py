N = int(input())
B = list(map(int,input().split()))
sB = set(B)
mc = B.count(max(sB,key=B.count))

print(str(mc)+" "+str(len(sB)))
