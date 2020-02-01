num = 0
cnt = 0
while True:
    sn = input('Enter Value:',)
    if sn == 'done':
        break
    try:
        fn = float(sn)

    except:
        fn = 0
        print('Enter valid number')
        continue
    if fn < 0:
        print('Enter positive numbers only')
        continue
    elif fn > 0:
        num = num + fn
        cnt = cnt + 1
print('total is:',num)
print('count is:',cnt)
