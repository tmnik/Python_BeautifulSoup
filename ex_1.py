# Read the HTML from the data files below, and parse the data, 
# extracting numbers and compute the sum of the numbers in the file
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
consts = list()
tags = soup('span')
for tag in tags:
    const = int(tag.contents[0])
    consts.append(const)
sumn = sum(consts)
print(sumn)
