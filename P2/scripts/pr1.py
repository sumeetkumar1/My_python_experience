while True:
    import re
    numlst = list()
    fn = input('Enter File name: ')
    try:
        fh = open(fn)
    except:
        print('Invalid Name')
        continue
    for ln in fh:
        ln = ln.rstrip()
        nu = re.findall('[0-9]+', ln)
    if len(nu) <= 0 : continue
    for num in nu:
        numi = int(num)
        numlst.append(numi)
    print(numlst)
