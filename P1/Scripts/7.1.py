fn = input('Enter File Name: ',)
try:
    fh = open(fn)
except:
    print('Enter Correct file name',)
    quit()
for line in fh:
    line = line.rstrip()
    line = line.upper()
    print(line)
