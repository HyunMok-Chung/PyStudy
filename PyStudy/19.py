t = int(input())

for i in range(t):
    cal = list(input().split())
    num = float(cal[0])
    for j in range(1, len(cal)):
        if cal[j] == "@":
            num *= 3
        elif cal[j] == "%":
            num += 5
        else:
            num -= 7
    print("%0.2f" % num)