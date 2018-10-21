a = int(input())

if a == 2000:
    print(str('12') + '/' + str('09') + '/' + str(a))
    exit(0)
if a % 400 == 0 or a % 4 == 0 and a % 100 != 0:
    if len(str(a)) == 1:
        print(str('12') + '/' + str('09') + '/' + str('000') + str(a))
    elif len(str(a)) == 2:
        print(str('12') + '/' + str('09') + '/' + str('00') + str(a))
    elif len(str(a)) == 3:
        print(str('12') + '/' + str('09') + '/' + str('0') + str(a))
    else:
        print(str('12') + '/' + str('09') + '/' + str(a))
else:
    if len(str(a)) == 1:
        print(str('13') + '/' + str('09') + '/' + str('000') + str(a))
    elif len(str(a)) == 2:
        print(str('13') + '/' + str('09') + '/' + str('00') + str(a))
    elif len(str(a)) == 3:
        print(str('13') + '/' + str('09') + '/' + str('0') + str(a))
    else:
        print(str('13') + '/' + str('09') + '/' + str(a))