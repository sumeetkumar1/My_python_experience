hrs = input('Enter Hours:')
h = float(hrs)
pay = input('Enter pay:')
p = float(pay)
if h>40:
    print('overtime')
    base = h*p
    otp = (h-40.0)*(p*0.5)
    TP = base+otp 
    print('The pay is:',TP)
else:
    tp=h*p
    print('The pay is:',tp)
quit()
