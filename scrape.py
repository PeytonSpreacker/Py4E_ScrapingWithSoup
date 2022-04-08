from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignores SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
counts = 0
sum = 0

# Retrieves all the <span> tags in the file
tags = soup('span')
for tag in tags:
    # Look at part of the tag
    # print('TAG', tag)
    # print('URL', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)
    num = int(tag.contents[0])
    sum = sum + num
    counts = counts + 1
print('Count', counts)
print('Sum', sum)
