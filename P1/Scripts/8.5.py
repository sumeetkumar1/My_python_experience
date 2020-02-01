fn = input('Enter File name: ')
try:
    fh = open(fn)
except:
    print('Invalid name')
    quit()
c = 0
for el in fh:
    if el.startswith('From '):
        c = c + 1
        strl = el.rstrip()
        slst = strl.split()
        print(slst[1])
print('There were',c,'lines in the file with From as the first word')
