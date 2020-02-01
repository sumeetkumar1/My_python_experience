# importing required libs for url, xml and ssl
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
# ignoring ssl file errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# Asking user to input URl and opening it
url = input("Enter URL: ")
html = urllib.request.urlopen(url, context=ctx).read()
# converting xml code got from the url for python processing.
tree = ET.fromstring(html)
lst = tree.findall('comments/comment')
valuelst = list()
# going through the xml code to find the count
for counts in lst:
    count = counts.find('count').text
    count = int(count)
    valuelst.append(count)
# adding and printing
print("sum is:", sum(valuelst))