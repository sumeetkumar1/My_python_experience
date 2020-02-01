s = input('Enter Score:',)
try:
    scr = float(s)
except:
    scr=0
    print('Enter numbers only')
    quit()
if scr < 0.0:
    print('Enter valid number')
elif scr > 1.0:
    print('Enter valid number')
elif scr >= 0.9:
    print('A')
elif scr >= 0.85:
    print('B')
elif scr >= 0.75:
    print('C')
elif scr >= 0.6:
    print('D')
elif scr < 0.6:
    print('F')
quit()
