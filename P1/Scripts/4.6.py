def computepay(h,r):
    if h>40:
        TP=(40.0*r)+((h-40.0)*r*1.5)
        return(TP)
    else:
        tp=h*r
        return(tp)

hrs = input("Enter Hours:")
try:
    ch = float(hrs)
except:
    ch = 0
    print('Enter valid number')
    quit()
rate = input('Enter Rate:',)
try:
    cr = float(rate)
except:
    cr = 0
    print('Enter valid number')
    quit()

p = computepay(ch,cr)
print('The pay is:',p)
