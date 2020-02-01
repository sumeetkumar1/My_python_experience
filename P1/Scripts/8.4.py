
fn = input('Enter file name: ')
try:
    fh = open(fn)
except:
    print('Invalid name')
    quit()
lst = list()
for line in fh:
    y = line.rstrip()
    wl = y.split()
    for cw in wl:
        if cw not in lst:
            lst.append(cw)
lst.sort()
print(lst)
