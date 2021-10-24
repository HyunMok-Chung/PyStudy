hour, min = map(int, input().split())

cooktime = int(input())

if min+cooktime >= 60:
    min2 = (min+cooktime)%60 #나머지
    hour += (min+cooktime)//60 #몫
    if hour >= 24:
        hour -= 24

else:
    min2 = min + cooktime

print(hour, min2)