# reading file name
fn = input('Enter file name: ')
# making sure user enters valid file name
try:
    fh = open(fn)
except:
    print('Invalid Name')
    quit()
# creating dictionary & list
counts = dict()
lst = list()
# reading through the file
for ln in fh:
# finding the required line
    if ln.startswith('From '):
        ln = ln.rstrip()
        ln = ln.split()
# extracting the hours
        ln.pop(0)
        ln.pop(0)
        ln.pop(0)
        ln.pop(0)
        ln.pop(0)
        ln.pop(1)
        hrs = ln[0]
# extracting only the hour data
        hrs = hrs.split(':')
        hrs.pop(1)
        hrs.pop(1)
# counting the number of hours
        for hrc in hrs:
            counts[hrc] = counts.get(hrc, 0) + 1
# sorting the count by hours and printing the data 
for k, v in sorted(counts.items()):
    print(k, v)
