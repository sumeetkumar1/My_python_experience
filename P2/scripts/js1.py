# importing the require lib
import urllib.request, urllib.parse, urllib.error
import ssl
import json
# ignoring ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#taking url form user
url = input("Enter url:")
data = urllib.request.urlopen(url, context=ctx)
# formatting JSON file
info = json.loads(data.read().decode('utf-8'))
count = list()
lst = info["comments"]
# going though the list and forming a list of counts and summing it
for cnt in lst:
    num = cnt.get('count')
    count.append(int(num))
print("Sum is:", sum(count))
