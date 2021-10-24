t = int(input())

for i in range(t):
    r, s = input().split()
    r = int(r)
    for j in s:
        print(j*r, end='') #end='' 옆으로 붙임
    print() #줄넘김