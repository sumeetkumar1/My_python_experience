import urllib.parse, urllib.error, urllib.parse
from bs4 import BeautifulSoup as BS
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter Url:", )
html = urllib.request.urlopen(url, context = ctx)
structuredhtml = BS(html, "html.parser")

tree = ET.fromstring(html)
lst = tree.findall()