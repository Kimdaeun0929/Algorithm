h, m = map(int, input(). split())
c = int(input())
if ((m+c) >=60):
    if ((h + ((m+c)//60))>=24) :
        print(((h+((m+c)//60))-24), ((m + c) - (60 * ((m + c) // 60))))
    else:
        print((h + ((m + c) // 60)), ((m + c) - (60 * ((m + c) // 60))) )
else:
    print(h, (m+c))