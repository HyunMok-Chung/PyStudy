a = int(input())
b = input()

x = int(b[0]) #문자열 첫 자리부터 0으로 시작
y = int(b[1])
z = int(b[2])

print(a*z)
print(a*y)
print(a*x)
print(a*x*100 + a*y*10 + a*z)