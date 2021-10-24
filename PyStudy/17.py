hr, min, sec = map(int, input().split())
cook = int(input())

if sec+cook >= 60:
    sec2 = (sec+cook)%60
    min += (sec+cook)//60
    if min >= 60:
        min2 = min%60
        hr += min//60
        if hr >=24:
            hr -= 24
            print(hr, min2, sec2)
        else:
            print(hr, min2, sec2)
    else:
        print(hr, min, sec2)
else:
    sec2 = sec+cook
    print(hr, min, sec2)