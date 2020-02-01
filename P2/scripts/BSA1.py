# Importing urllib, BeautifulSoup and ssl for Processing HTML files
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup, ResultSet
import ssl
# Ignoring SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# getting user input as well as ignoring SSl and creating a soup
url = input("Enter Url: ")
html = urllib.request.urlopen(url, context=ctx).read()
soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')
# Extracting <span>
values: ResultSet = soup('span')
# crating a list for number that are extracted
numlst = list()
# extracting the contents of <span> and converting it to Integer values and finding sum
for value in values:
    x = value.contents[0]
    xint = int(x)
    numlst.append(xint)
print('Sum:', sum(numlst))
