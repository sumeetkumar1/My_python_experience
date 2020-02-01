fn = input('Enter the file name: ')
s = 0.0
c = 0
try:
    fh = open(fn)
except:
    print('Enter valid file name')
    quit()
for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        c = c + 1
        line = line.rstrip()
        dp = line.find('0')
        #sp = line.find(' ', dp)
        cd = line[dp : 26]
        try:
            fd = float(cd)
        except:
            fd = 0
            print('Numbers only!')
            quit()
        s = s + fd
print('Average spam confidence:',s/c)
