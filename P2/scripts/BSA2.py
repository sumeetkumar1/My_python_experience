# importing the required Libraries/
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Taking User Input
url = input("Enter Url:")
count = input("Enter Count:",)
position = input("Enter Position:",)
# testing User Input
try:
    count = int(count)
    position = int(position)
except:
    print("Enter Valid Count or Position")
    quit()
# Ignoring SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# Forming loops for the url to be opened multiple times. In the First for loop the users URL is considered.
# The next for loop extracts the required URL
# at the end of the 2nd for loop the variable 'url' is changed to the url at position mention.
# this processes is repeated for the 'range of counts'
#while count > 0:
    #count = count - 1
#(or)
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    strhtm: BeautifulSoup = BeautifulSoup(html, "html.parser")
    links = strhtm("a")
    lnklst = list()
    for link in links:
        lnk = link.get("href", None)
        lnklst.append(lnk)
    url = lnklst[position - 1]
    print(url)
