# getting file name from the user
fn = input('Enter file name: ')
import re
numlst = list()
try:
    fh = open(fn)
except:
    print('Invalid Name')
    quit()
# going through the file and finding numbers
for ln in fh:
    ln = ln.rstrip()
    num = re.findall('[0-9]+', ln)
# Making sure the list produced after the search has numbers
    if len(num) <= 0: continue
# converting the numbers to integers and forming a single list
    for numb in num:
        nu = int(numb)
        numlst.append(nu)
# Suming and printing the answer 
print(sum(numlst))
