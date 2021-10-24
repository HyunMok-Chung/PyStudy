a, b, c = map(int, input().split())

if a>=b:
    if b>=c:
        print(b)
    elif b<c:
        if a>=c:
            print(c)
        else:
            print(a)
else:
    if a>=c:
        print(a)
    elif a<c:
        if c<=b:
            print(c)
        else:
            print(b)