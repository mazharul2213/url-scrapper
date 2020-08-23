#URL Scrapping program
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#handling ssl error certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#sending request for datq
url = input("Enter URL: ")
if len(url) < 1:
    url = "http://dr-chuck.com"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#data from requesr
tags = soup('span class="comments')
for tag in tags:
    data = tag.get('href', None)
    if data.startswith("http"):
        #print(tag.get('href', None))
        print(data)