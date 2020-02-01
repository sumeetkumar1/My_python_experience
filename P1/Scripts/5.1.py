lrg = -1
sml = None
while True:
    sv = input ('Enter the number:',)
    if sv == 'Done':
        break
    try:
        fv = int(sv)
    except:
        fv = 0
        print ('Enter Valid Number')
        continue
    if fv > lrg:
        lrg = fv
    if sml is None:
        sml = fv
    elif fv < sml:
        sml = fv
print ('Max',lrg)
print ('Min',sml)
