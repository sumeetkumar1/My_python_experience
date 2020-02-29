fn = input("Enter File name: ")
fh = open(fn)

for line in fh:
    if line.startswith('From: '):
        lines = line.split()
        email = lines[1]
        doms = email.split('@')
        org = doms[1]
        print(org)
l