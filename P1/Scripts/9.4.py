# Entering a file name
fn = input('Enter File name: ')
try:
    fh = open(fn)
except:
    print('Invalid name')
    quit()
counts = dict() # creating a Dictionary

for el in fh:
    if el.startswith('From '):
# creating a list of only email address
        strl = el.rstrip()
        eml = strl.split()
# removing uwanted elements from the list
        eml.pop(0)
        eml.pop(1)
        eml.pop(1)
        eml.pop(1)
        eml.pop(1)
        eml.pop(1)
        for email in eml:
            counts[email]=counts.get(email,0) + 1
# finding the largest number
bigcount = None
bigword = None
for k, v in counts.items():
    if bigcount is None or v > bigcount:
        bigword = k
        bigcount = v
print(bigword,bigcount)
